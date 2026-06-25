# AI Workflow Architecture

## Purpose

This reference architecture turns an AI request into a controlled operational workflow. It is designed for creative, technical, and operational teams that need to move beyond ad hoc prompting while retaining speed.

## Core lifecycle

```text
1. Intake
2. Scope and classify the request
3. Select approved knowledge basis
4. Select prompt lineage
5. Select provider route
6. Generate or assist
7. Evaluate against task-specific criteria
8. Record witness and review conditions
9. Human review and release decision
10. Monitor for material change
11. Revalidate or retire the standing
12. Preserve replay and audit evidence
```

## Operating model

| Layer | Question | Example control |
|---|---|---|
| Intake | What is being requested and for whom? | Use-case owner, audience, risk category, intended channel |
| Knowledge basis | What material may support the output? | Approved source IDs, owners, versions, effective dates |
| Prompt lineage | Which instruction artifact shaped the work? | Prompt ID, version, approval status, change notes |
| Provider route | Which model or service path is being used? | Provider, model/mode, data-handling profile, fallback |
| Evaluation | What must be true for use? | Accuracy, brand, legal, safety, format, completeness |
| Review | Who decides release? | Reviewer role, sign-off, exception record |
| Continuity | What later changes invalidate the result? | Source updates, policy change, prompt update, provider change |
| Replay | What can be inspected later? | Inputs, outputs, decisions, timestamps, reason codes |

## Why source basis is explicit

A useful AI output can still be operationally unsafe or misleading when its supporting material is unknown, stale, incomplete, or outside scope. The workflow therefore treats source selection as a visible and versioned step.

```text
unbounded request + invisible context
≠
reviewable operational output
```

Instead:

```text
scoped request + approved basis + declared prompt + declared route
+ evaluation + human review
= a reviewable release candidate
```

## Example request path

```text
Request:
Create a launch package for a product update.

Approved basis:
- product brief v1.0
- approved claims register v2026.06
- brand voice guide v1.4
- customer support FAQ v1.0

Prompt lineage:
Launch Package / v1.0

Provider route:
Evaluation route / dry-run

Evaluation conditions:
- claims must map to approved statements
- audience and channel must be specified
- unsupported claims must be refused or marked for review
- output must retain source traceability

Review outcome:
May bind after named reviewer approval.
```

## Revalidation logic

A prior approval should not remain silently current when a material condition changes.

Examples of material change:

- a source document is superseded;
- a claims register changes;
- a prompt changes in a way that affects behavior;
- a provider/model route changes;
- a policy or brand standard changes;
- an evaluation failure or incident occurs.

The proper behavior is not necessarily deletion. It is usually:

```text
preserve original record
→ mark the prior standing as requiring revalidation
→ resolve against current approved conditions
→ produce a new reviewable standing
```

## Implementation approach

The public sandbox uses browser-local state only. A production implementation would typically use:

- a document store and metadata registry;
- a retrieval or search layer appropriate to corpus size and data classification;
- a prompt registry with version control and evaluation sets;
- provider adapters with observability and fallback behavior;
- workflow state storage, audit records, and access controls;
- role-based review and exception handling;
- integration-specific policy checks.

That progression is intentional: prove workflow clarity first, then harden for the organization’s data, risk, scale, and integration requirements.
