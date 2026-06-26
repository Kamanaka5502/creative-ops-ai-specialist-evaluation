"""Run a task record through the deterministic public grader.

Usage:
    python3 evaluate.py --task tasks/creative.json --record samples/runs/run_001_human.json
    python3 evaluate.py --task tasks/creative.json --record samples/runs/run_001_human.json --output /tmp/evaluated.json

The runner uses standard-library shape validation. Full JSON contracts are in
schemas/task.schema.json and schemas/evaluation_record.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from graders.basic import grade

TASK_REQUIRED = {
    "task_id",
    "domain",
    "description",
    "input",
    "input_material",
    "risk_profile",
    "expected_behaviors",
    "grading_dimensions",
}
RECORD_REQUIRED = {
    "task_id",
    "trial_id",
    "agent_id",
    "material_basis",
    "prompt_lineage",
    "provider_route",
    "resolution",
    "witness",
    "reviewed_standing",
    "revalidation_events",
    "replay_trace",
}


def load_json(path: str) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def require_fields(value: dict[str, Any], required: set[str], label: str) -> None:
    missing = sorted(required - set(value))
    if missing:
        raise ValueError(f"{label} is missing required fields: {', '.join(missing)}")


def validate_task(task: dict[str, Any]) -> None:
    require_fields(task, TASK_REQUIRED, "Task")
    if not task["input"].get("movement") or not task["input"].get("intended_use"):
        raise ValueError("Task input requires movement and intended_use.")
    if not isinstance(task["input_material"], list) or not task["input_material"]:
        raise ValueError("Task input_material must contain at least one material fixture.")


def validate_record(record: dict[str, Any]) -> None:
    require_fields(record, RECORD_REQUIRED, "Evaluation record")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a consequence record against a task definition.")
    parser.add_argument("--task", required=True, help="Path to task JSON.")
    parser.add_argument("--record", required=True, help="Path to evaluation record JSON.")
    parser.add_argument("--output", help="Optional path for a graded evaluation artifact.")
    args = parser.parse_args()

    task = load_json(args.task)
    record = load_json(args.record)
    validate_task(task)
    validate_record(record)
    result = grade(task, record)
    artifact = {"task": task, "record": record, "evaluation": result}
    rendered = json.dumps(artifact, indent=2, sort_keys=True)

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
        print(f"Wrote evaluation artifact: {output}")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
