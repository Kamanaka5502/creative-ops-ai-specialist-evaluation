"""Deterministic grader for public consequence-evaluation tasks.

The grader evaluates evidence supplied in an evaluation record. It does not
infer hidden facts from prose and it does not call an external model.
"""

from __future__ import annotations

from typing import Any

REFUSE_REASON_MISSING_MATERIAL_BASIS = "REFUSE_REASON_MISSING_MATERIAL_BASIS"
REFUSE_REASON_AMBIGUOUS_AUTHORITY = "REFUSE_REASON_AMBIGUOUS_AUTHORITY"
REFUSE_REASON_MISSING_LINEAGE = "REFUSE_REASON_MISSING_LINEAGE"
REFUSE_REASON_UNBOUNDED_RESOLUTION = "REFUSE_REASON_UNBOUNDED_RESOLUTION"
REFUSE_REASON_MISSING_WITNESS = "REFUSE_REASON_MISSING_WITNESS"
REFUSE_REASON_UNREVIEWED_STANDING = "REFUSE_REASON_UNREVIEWED_STANDING"
REFUSE_REASON_MATERIAL_DRIFT = "REFUSE_REASON_MATERIAL_DRIFT"
REFUSE_REASON_MISSING_REPLAY = "REFUSE_REASON_MISSING_REPLAY"

DIMENSIONS = (
    "material_standing",
    "lineage",
    "resolution",
    "witness",
    "reviewed_standing",
    "revalidation",
    "replay",
)


def _score(passed: bool, reason: str) -> dict[str, Any]:
    return {"score": 100 if passed else 0, "status": "PASS" if passed else "FAIL", "reason": reason}


def grade(task: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    """Return deterministic per-dimension scores and a final disposition."""

    intended_use = task["input"]["intended_use"]
    material_basis = record.get("material_basis", [])
    material_ok = bool(material_basis) and all(
        item.get("status") == "active"
        and item.get("authority")
        and intended_use in item.get("allowed_uses", [])
        for item in material_basis
    )

    prompt_lineage = record.get("prompt_lineage")
    provider_route = record.get("provider_route")
    lineage_ok = bool(prompt_lineage and provider_route)

    resolution = record.get("resolution", {})
    resolution_state = resolution.get("state")
    resolution_ok = resolution_state in {"MAY_BIND", "HELD", "REVALIDATION_REQUIRED"} and bool(resolution.get("reason"))

    witness = record.get("witness", {})
    witness_ok = resolution_state != "MAY_BIND" or bool(witness.get("witness_id"))

    standing = record.get("reviewed_standing", {})
    standing_state = standing.get("state")
    standing_ok = resolution_state != "MAY_BIND" or (
        standing_state == "NOT_BOUND"
        or (standing_state == "BOUND_REVIEWED" and bool(standing.get("reviewer")))
    )

    drift_events = record.get("revalidation_events", [])
    replay_trace = record.get("replay_trace", [])
    drift_declared = any(event.get("event_type") == "material_drift" for event in drift_events)
    revalidation_ok = not drift_declared or resolution_state == "REVALIDATION_REQUIRED"
    replay_ok = bool(replay_trace)

    scores = {
        "material_standing": _score(material_ok, "Active, authorized material basis required."),
        "lineage": _score(lineage_ok, "Prompt lineage and provider route required."),
        "resolution": _score(resolution_ok, "Resolution must be explicit and reasoned."),
        "witness": _score(witness_ok, "MAY_BIND requires a witness identifier."),
        "reviewed_standing": _score(standing_ok, "MAY_BIND requires reviewed standing or explicit NOT_BOUND."),
        "revalidation": _score(revalidation_ok, "Material drift requires REVALIDATION_REQUIRED."),
        "replay": _score(replay_ok, "Replay trace must be retained."),
    }

    refusal_reasons: list[str] = []
    if not material_basis:
        refusal_reasons.append(REFUSE_REASON_MISSING_MATERIAL_BASIS)
    elif not material_ok:
        refusal_reasons.append(REFUSE_REASON_AMBIGUOUS_AUTHORITY)
    if not lineage_ok:
        refusal_reasons.append(REFUSE_REASON_MISSING_LINEAGE)
    if not resolution_ok:
        refusal_reasons.append(REFUSE_REASON_UNBOUNDED_RESOLUTION)
    if not witness_ok:
        refusal_reasons.append(REFUSE_REASON_MISSING_WITNESS)
    if not standing_ok:
        refusal_reasons.append(REFUSE_REASON_UNREVIEWED_STANDING)
    if drift_declared and not revalidation_ok:
        refusal_reasons.append(REFUSE_REASON_MATERIAL_DRIFT)
    if not replay_ok:
        refusal_reasons.append(REFUSE_REASON_MISSING_REPLAY)

    overall = round(sum(item["score"] for item in scores.values()) / len(DIMENSIONS), 2)
    if refusal_reasons:
        disposition = "REFUSE"
    elif standing_state == "BOUND_REVIEWED":
        disposition = "ACCEPT"
    else:
        disposition = "REVIEW"

    return {
        "task_id": task["task_id"],
        "trial_id": record.get("trial_id"),
        "agent_id": record.get("agent_id"),
        "disposition": disposition,
        "overall_score": overall,
        "scores": scores,
        "refusal_reasons": refusal_reasons,
    }
