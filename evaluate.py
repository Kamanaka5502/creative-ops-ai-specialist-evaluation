"""Run a task record through the deterministic public grader.

Usage:
    python3 evaluate.py --task tasks/creative.json --record samples/runs/run_001_human.json
    python3 evaluate.py --task tasks/creative.json --record samples/runs/run_001_human.json --output /tmp/evaluated.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from graders.basic import grade


def load_json(path: str) -> dict:
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a consequence record against a task definition.")
    parser.add_argument("--task", required=True, help="Path to task JSON.")
    parser.add_argument("--record", required=True, help="Path to evaluation record JSON.")
    parser.add_argument("--output", help="Optional path for a graded evaluation artifact.")
    args = parser.parse_args()

    task = load_json(args.task)
    record = load_json(args.record)
    result = grade(task, record)
    artifact = {"record": record, "evaluation": result}
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
