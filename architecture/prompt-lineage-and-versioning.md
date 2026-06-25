# Prompt Lineage and Versioning

## Position

Prompts are operational artifacts. When a prompt influences customer-facing, decision-support, creative, technical, or support work, it should be governed with the same basic discipline applied to other production assets: identity, ownership, versioning, testing, approval, and rollback.

## Prompt record

A prompt registry entry can be lightweight while still being useful.

```yaml
prompt_id: PRM-LAUNCH-PACKAGE
name: Launch Package Composer
version: 1.0
owner: Creative Operations
status: active
purpose: Create a structured launch package from approved basis materials.
inputs:
  - product_brief
  - approved_claims
  - brand_voice
  - audience
outputs:
  - landing_page_copy
  - customer_support_response
  - voiceover_outline
  - storyboard
constraints:
  - do not invent product claims
  - identify unsupported requests
  - preserve source references in internal trace
review_required: true
last_evaluated: 2026-06-25
change_notes: Initial public evaluation example.
```

## Minimum lifecycle

```text
draft
→ peer review
→ evaluation against representative inputs
→ approve
→ active
→ monitor
→ revise or deprecate
→ retain prior version and change rationale
```

## What should change a prompt version

Create a new version when there is a material change to:

- system instructions or output constraints;
- retrieval behavior or source-selection logic;
- model/provider route assumptions;
- safety or escalation rules;
- output schema;
- audience, brand, legal, or compliance rules;
- evaluation expectations.

Copy edits that do not materially change behavior can be handled with a documented minor revision policy.

## Evaluation dimensions

A practical prompt evaluation set can score:

| Dimension | Review question |
|---|---|
| Task completion | Did the output complete the requested work? |
| Grounding | Did it stay within approved source material? |
| Instruction adherence | Did it follow format and workflow constraints? |
| Factuality | Did it avoid unsupported statements? |
| Style | Did it meet brand, audience, and clarity expectations? |
| Safety | Did it surface uncertainty and refuse unsafe requests? |
| Consistency | Is behavior stable across representative examples? |
| Efficiency | Is quality acceptable for cost and latency? |

## Change control example

```text
Prompt v1.0
- supports launch copy
- uses approved claims register

Prompt v1.1
- adds a mandatory source-gap marker for unsupported claims
- adds a handoff section for legal review

Required follow-up:
- run targeted evaluation set
- compare output against v1.0
- confirm no undesired formatting or style regression
- document approval and rollout timing
```

## Why lineage matters

Without prompt lineage, a later reviewer cannot reliably distinguish whether a changed result came from:

- altered source material;
- a prompt update;
- a provider/model update;
- a changed user request;
- a human editing step;
- a retrieval or tool-routing change.

Visible lineage turns that ambiguity into an inspectable workflow record.

## Sample

See `samples/prompt-library-example.md` for a compact prompt-library pattern suitable for an internal working repository.
