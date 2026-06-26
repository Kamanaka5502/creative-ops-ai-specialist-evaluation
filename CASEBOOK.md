# Operational Intelligence Casebook

These are reference applications of the architecture in this public repository. They show how the same consequence model adapts to different work without collapsing into a single generic AI workflow.

## 1. Creative launch movement

### Proposed movement

Release customer-facing launch material across landing page, support, voice, and visual channels.

### Active field

```text
product authority
+ approved claims
+ brand constraints
+ campaign constraints
+ channel-specific release conditions
```

### What the system resolves

- Are the claims supported by the active basis?
- Is the requested channel covered by the current constraints?
- Which prompt lineage and provider route produced the artifact?
- What review must occur before public release?
- What source change makes the prior release stale?

### What binds consequence

Not generation. A named reviewer binds the standing after the source basis, claim scope, channel conditions, and output checks are satisfied.

### Drift example

A claims register changes after creative assets are drafted. The previous materials remain replayable, but they are not treated as current until re-resolved.

---

## 2. Customer-support assistance movement

### Proposed movement

Prepare a support response that may influence customer action, expectation, or escalation.

### Active field

```text
approved FAQ
+ current product state
+ policy and entitlement boundaries
+ account-context availability
+ escalation rules
```

### What the system resolves

- Is the answer grounded in active support authority?
- Is account-specific information missing?
- Does the request involve privacy, billing, legal, safety, or access conditions requiring a handoff?
- Is the system being asked to promise something not supported by the basis?

### What binds consequence

The output may support an operator or enter a review queue. It does not replace the escalation rule, the authoritative policy, or the decision owner.

### Drift example

A return-policy change or service incident invalidates prior response templates. The system should preserve prior output history while forcing current resolution against the updated field.

---

## 3. AI-assisted technical change movement

### Proposed movement

Use AI to generate a code change, infrastructure configuration, migration plan, or technical operations artifact.

### Active field

```text
repository state
+ architecture constraints
+ approved dependency policy
+ test and release criteria
+ environment / deployment conditions
```

### What the system resolves

- Is the requested change in scope for the repository and environment?
- Does generated output conflict with established architectural constraints?
- What test evidence is required before merge or release?
- Which model route and prompt lineage participated in the proposed change?
- What dependency, specification, or environment change requires revalidation?

### What binds consequence

The movement becomes real through code review, test evidence, deployment controls, and explicit rollback conditions—not because a model emitted syntactically valid code.

### Drift example

A dependency update, policy revision, or target-environment change reopens validation even if the earlier generated change was previously approved.

---

## 4. Model-adaptation movement

### Proposed movement

Adapt a model or route behavior through LoRA or another constrained model-adaptation approach.

### Active field

```text
authorized training corpus
+ data provenance and classification
+ base-model reference
+ task-specific evaluation set
+ safety and refusal criteria
+ rollback route
```

### What the system resolves

- Is adaptation actually required, or would retrieval, prompting, structured outputs, or workflow design solve the problem more safely?
- Is the dataset authorized, representative, versioned, and suitable for the target task?
- Does the adapted behavior outperform the baseline on held-out evaluation?
- Does it preserve required refusal and escalation behavior?
- What new data, base-model, or policy change requires re-evaluation?

### What binds consequence

An adapter is not operationally valid because it trained. It requires evidence-based acceptance against the defined task, safety, reliability, latency, cost, and rollback conditions.

### Drift example

A base-model change, a material shift in task distribution, or a change in data rights triggers re-evaluation of the adaptation standing.

---

## 5. Cross-functional AI adoption movement

### Proposed movement

Introduce a new AI capability into a creative, operations, support, or technical team.

### Active field

```text
business objective
+ workflow owner
+ user roles
+ data boundary
+ task evaluation
+ provider decision
+ enablement protocol
+ release and incident path
```

### What the system resolves

- Is the use case specific enough to evaluate?
- Who owns the workflow once the prototype works?
- What data can enter the tool and what must remain outside it?
- How will quality, adoption, cost, risk, and failure be observed?
- What does a user do when the system cannot establish sufficient basis?

### What binds consequence

A team does not adopt a tool merely because a demo is impressive. Adoption becomes real when an owned operating path, clear constraints, evaluation evidence, and practical user protocol exist.

## Through-line

The same architecture scales across these domains because the invariant is not the tool. It is the question of standing:

```text
What movement is proposed?
What active field governs it?
What proof exists?
Who can bind it?
What change invalidates its prior standing?
```
