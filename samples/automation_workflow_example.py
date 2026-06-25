"""Lightweight AI workflow evaluation example.

This public sample demonstrates a compact implementation pattern for:
- validating an active source basis;
- carrying prompt and provider context;
- producing a structured outcome;
- emitting a deterministic witness payload.

It makes no network calls and uses no external AI provider.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Iterable, Literal

SourceStatus = Literal["approved", "draft", "deprecated", "blocked"]
Resolution = Literal["BIND", "HALT", "REVALIDATE"]
Permission = Literal["MAY_BIND", "NOT_BOUND"]


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    title: str
    version: str
    status: SourceStatus
    allowed_uses: tuple[str, ...]


@dataclass(frozen=True)
class WorkflowRequest:
    request_id: str
    request_text: str
    intended_use: str
    prompt_id: str
    prompt_version: str
    provider_route: str
    source_ids: tuple[str, ...]


@dataclass(frozen=True)
class WorkflowOutcome:
    resolution: Resolution
    permission: Permission
    reasons: tuple[str, ...]
    required_conditions: tuple[str, ...]
    witness_id: str | None


def resolve_workflow(
    request: WorkflowRequest,
    sources: Iterable[SourceRecord],
) -> WorkflowOutcome:
    """Evaluate whether a request has a sufficient approved basis.

    This is intentionally simple. A production implementation would add access
    controls, policy routing, retrieval evaluation, richer risk classification,
    persistence, audit storage, and task-specific quality checks.
    """

    source_map = {source.source_id: source for source in sources}
    selected = [source_map[source_id] for source_id in request.source_ids if source_id in source_map]

    if not request.request_text.strip():
        return WorkflowOutcome(
            resolution="HALT",
            permission="NOT_BOUND",
            reasons=("Request text is empty.",),
            required_conditions=("Provide a scoped workflow request.",),
            witness_id=None,
        )

    if not selected:
        return WorkflowOutcome(
            resolution="HALT",
            permission="NOT_BOUND",
            reasons=("No approved source material is active.",),
            required_conditions=("Select at least one approved source record.",),
            witness_id=None,
        )

    invalid = [source for source in selected if source.status != "approved"]
    if invalid:
        names = ", ".join(f"{source.title} ({source.status})" for source in invalid)
        return WorkflowOutcome(
            resolution="HALT",
            permission="NOT_BOUND",
            reasons=(f"Selected sources are not approved: {names}.",),
            required_conditions=("Replace unapproved, blocked, or deprecated sources.",),
            witness_id=None,
        )

    unsupported = [source.title for source in selected if request.intended_use not in source.allowed_uses]
    if unsupported:
        return WorkflowOutcome(
            resolution="HALT",
            permission="NOT_BOUND",
            reasons=(f"Selected sources do not authorize intended use '{request.intended_use}': {', '.join(unsupported)}.",),
            required_conditions=("Use sources approved for the intended workflow.",),
            witness_id=None,
        )

    witness_id = make_witness_id(request, selected)
    return WorkflowOutcome(
        resolution="BIND",
        permission="MAY_BIND",
        reasons=(
            "Scoped request is present.",
            "Active sources are approved.",
            "Active sources permit the intended use.",
            "Prompt lineage and provider route are declared.",
        ),
        required_conditions=(
            "Human review is required before external release.",
            "Revalidate if source, prompt, provider route, policy, or intended use changes.",
        ),
        witness_id=witness_id,
    )


def make_witness_id(request: WorkflowRequest, sources: Iterable[SourceRecord]) -> str:
    """Create a deterministic demonstration witness identifier."""

    basis = {
        "request": asdict(request),
        "sources": [asdict(source) for source in sorted(sources, key=lambda item: item.source_id)],
        "created_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
    }
    digest = sha256(repr(basis).encode("utf-8")).hexdigest()[:16].upper()
    return f"WIT-{digest}"


def example() -> None:
    sources = (
        SourceRecord(
            source_id="SRC-PRODUCT-BRIEF-001",
            title="Feature Product Brief",
            version="1.0",
            status="approved",
            allowed_uses=("product_marketing", "support_enablement"),
        ),
        SourceRecord(
            source_id="SRC-CLAIMS-REGISTER-001",
            title="Approved Claims Register",
            version="2026.06",
            status="approved",
            allowed_uses=("product_marketing",),
        ),
    )
    request = WorkflowRequest(
        request_id="REQ-DEMO-001",
        request_text="Draft a product launch announcement using the approved basis.",
        intended_use="product_marketing",
        prompt_id="PRM-LAUNCH-PACKAGE",
        prompt_version="1.0",
        provider_route="evaluation-route/dry-run",
        source_ids=("SRC-PRODUCT-BRIEF-001", "SRC-CLAIMS-REGISTER-001"),
    )
    outcome = resolve_workflow(request, sources)
    print(outcome)


if __name__ == "__main__":
    example()
