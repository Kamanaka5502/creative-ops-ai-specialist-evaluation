# Evaluation System

## Execution path

```text
Task definition
→ evaluation record
→ deterministic grader
→ structured scores and refusal reasons
→ replayable run artifact
```

## Task catalog

- `tasks/creative.json` — reviewed creative launch movement
- `tasks/technical.json` — AI-assisted technical change movement
- `tasks/ops.json` — operations routing movement

Each task contains the movement input, expected behaviors, risk profile, and grading dimensions.

## Data contract

`schemas/evaluation_record.json` defines the record shape:

```text
task_id
trial_id
agent_id
material_basis
prompt_lineage
provider_route
resolution
witness
reviewed_standing
revalidation_events
replay_trace
```

## Deterministic grading

`graders/basic.py` returns structured scores for:

```text
material_standing
lineage
resolution
witness
reviewed_standing
revalidation
replay
```

It also returns an explicit disposition:

```text
ACCEPT
REVIEW
REFUSE
```

## Run the evaluator

```bash
python3 evaluate.py \
  --task tasks/creative.json \
  --record samples/runs/run_001_human.json \
  --output /tmp/creative-evaluation.json
```

## Evidence runs

- `samples/runs/run_001_human.json` — reviewed, accepted standing
- `samples/runs/run_002_ai_copilot.json` — complete record, explicitly not bound pending review
- `samples/runs/run_003_agent.json` — refusal artifact for an attempted bypass

The run artifacts are illustrative and deterministic. They are not claims about a real person, provider, or production environment.

## Test surface

```bash
python3 -m unittest tests/test_basic_grader.py
```

The tests cover every grading dimension plus a bypass attempt that must be refused.

## Failure-closed boundary

The grader names refusal conditions in `graders/basic.py`. Their operational meaning is documented in `SAFE_EVALUATION_BOUNDARY.md`.
