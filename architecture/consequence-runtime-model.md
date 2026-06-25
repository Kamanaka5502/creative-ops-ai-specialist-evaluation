# Consequence-Bound Operational Intelligence Model

## The problem

Most AI implementations begin with a generation question:

```text
Can the system produce a useful artifact?
```

That question is necessary but incomplete in an operational setting.

The governing question is:

```text
May this proposed movement become real under the conditions currently in force?
```

The difference matters whenever AI-supported work influences customers, internal operations, claims, creative releases, technical change, support guidance, or organizational decisions.

## The model

A proposed movement is evaluated against a visible field of conditions.

```text
M = proposed movement
B = active material basis
L = lineage: prompt, source versions, provider route
C = applicable conditions and constraints
W = witness of the resolution state
S = reviewed standing
Δ = later material change
```

The architecture is concerned with the transition:

```text
(M, B, L, C) → resolve → W → S
```

A standing is current only while its material conditions remain valid.

```text
If Δ changes B, L, or C materially:

S → revalidate
```

This does not require deleting history. It requires preventing silent carry-forward of an earlier standing that no longer matches the active field.

## Layers of the field

| Layer | Role |
|---|---|
| Proposed movement | What action, output, or change is being considered? |
| Material basis | Which documents, facts, policy, constraints, and authority are active? |
| Lineage | Which prompt, source versions, provider route, and workflow path participated? |
| Conditions | What must be true before the movement can stand? |
| Witness | What records the reason, basis, and state of resolution? |
| Reviewed standing | What human or designated authority allows the movement to be used? |
| Revalidation | What happens when a later change makes the previous standing stale? |
| Replay | How can the system reconstruct what was active and why? |

## Component technologies are subordinate

RAG, agents, prompt libraries, provider APIs, LoRA adapters, workflows, and automation are useful only insofar as they help preserve or evaluate the field.

```text
RAG is not the architecture.
Prompting is not the architecture.
A provider route is not the architecture.
A dashboard is not the architecture.

They are mechanisms inside a consequence-bound operational system.
```

## Example: customer-facing launch content

```text
Proposed movement:
Publish launch package to an external audience.

Active material basis:
- approved product brief
- approved claims register
- brand voice guide
- campaign constraints

Lineage:
- launch prompt v1.0
- declared provider route
- source versions captured

Conditions:
- all factual claims map to current approved basis
- no unsupported promise is present
- channel-specific review is complete

Witness:
- records active materials, lineage, conditions, reviewer, and timestamp

Standing:
- reviewed release may proceed

Later change:
- claims register changes

Result:
- prior release remains inspectable
- prior standing requires revalidation before reuse
```

## Practical implementation

The public operational surface models this lifecycle in browser-local state. A real organization would implement the same structure using appropriate persistence, access controls, provider adapters, retrieval infrastructure, evaluation sets, observability, and human approval paths.

The architecture remains the same even as the tooling changes.
