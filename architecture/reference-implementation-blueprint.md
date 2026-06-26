# Reference Implementation Blueprint

## Purpose

This blueprint shows how the public consequence model can be implemented as an operational system without confusing a public demonstration with a production service.

The architecture begins with movement and standing, then selects the right technical mechanisms for the organization.

## System topology

```text
                     ┌──────────────────────────────┐
                     │        Intake surface         │
                     │ request · audience · use case │
                     └──────────────┬───────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────┐n│                    Operational resolution layer                    │
│ scope · material authority · lineage · conditions · risk routing   │
└───────┬──────────────────┬───────────────────┬─────────────────────┘
        │                  │                   │
        ▼                  ▼                   ▼
 material registry     prompt registry     provider adapters
 authority/version     version/evaluation  model/tool/route policy
        │                  │                   │
        └──────────────┬───┴──────────┬────────┘
                       ▼              ▼
                 retrieval field   generation/tool action
                       │              │
                       └───────┬──────┘
                               ▼
                    task-specific evaluation
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
          hold / escalate             witness + review queue
                                              │
                                              ▼
                                      reviewed standing
                                              │
                                              ▼
                              release / integration / deployment
                                              │
                                              ▼
                              drift detection + replay ledger
```

## Core entities

| Entity | Responsibility |
|---|---|
| Movement | A proposed action or artifact with an intended consequence |
| Material record | Source identity, authority, version, status, use scope, provenance |
| Prompt lineage | Prompt identity, version, evaluation status, owner, change note |
| Provider route | Model/tool choice, policy profile, fallback, observability requirements |
| Resolution | Determination of whether the current field is sufficient for review |
| Witness | Inspectable record of active field, reasons, conditions, and result |
| Reviewed standing | Named approval that permits the movement to proceed within conditions |
| Drift event | Material change that may invalidate the prior standing |
| Replay ledger | Ordered record used to reconstruct what happened and why |

## Separation of concerns

### Material authority

A material registry answers:

```text
What may stand behind this output?
Who owns it?
Which version is current?
For which uses is it valid?
```

This can be backed by controlled repositories, content systems, document stores, or enterprise knowledge platforms. Retrieval is one access mechanism, not the definition of authority.

### Generation and provider routing

Provider adapters answer:

```text
Which provider/model/tool route is appropriate for this movement?
What data boundary applies?
What fallback and failure behavior is required?
What route details must be recorded for later replay?
```

The system does not assume one provider or one model type. It retains a declared route so a later evaluator can understand the path that produced the proposed result.

### Evaluation

Task-specific evaluation answers:

```text
Did the proposed result satisfy the conditions of this movement?
Did it remain within material authority?
Did it produce an unsupported assertion, unsafe transformation, or incomplete artifact?
What should be held, escalated, or reviewed?
```

Evaluation can include deterministic checks, structured schema validation, retrieval quality checks, human review, domain rules, test suites, and model-graded signals where appropriate.

### Continuity

Continuity answers:

```text
What changed after the standing was reached?
Does the prior standing remain current?
What must be replayed, revalidated, or retired?
```

This layer is what prevents a system from treating a previously approved output as permanently valid after its basis has changed.

## Production hardening path

| Stage | Objective | Representative mechanisms |
|---|---|---|
| Proof | Establish the movement/standing model | Browser prototype, local fixtures, visible state transitions |
| Controlled pilot | Test within one owned workflow | Role-limited access, approved corpus, task evaluation set, review queue |
| Operational integration | Connect to real systems | Provider adapters, source synchronization, observability, permission model |
| Scaled service | Support multiple teams or workflows | Tenant boundaries, policy packs, event storage, monitoring, incident handling |
| High-assurance path | Support critical decisions | Domain validation, stronger evidence controls, formal review, change management |

## Failure behavior

The safe default is not to fabricate continuity.

```text
Missing basis → HOLD
Unknown authority → HOLD
Inactive or superseded material → HOLD
Lineage not declared → HOLD
Material drift after review → REVALIDATION_REQUIRED
Provider failure → HOLD or route to approved fallback
Evaluation uncertainty → ESCALATE
```

## Why this matters

A conventional AI implementation may answer, "The model produced a result." This architecture answers the operational question:

```text
What was allowed to influence the result,
what conditions made it reviewable,
what authority allowed it to stand,
and what later change would make it no longer current?
```
