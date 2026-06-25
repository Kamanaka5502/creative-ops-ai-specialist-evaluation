# Prompt Library Example

This is a compact example of how an internal prompt library can make AI-assisted work easier to reuse, evaluate, review, and improve.

## Prompt: Launch Package Composer

```yaml
prompt_id: PRM-LAUNCH-PACKAGE
version: 1.0
status: active_example
owner: Creative Operations
reviewer: Product Marketing
purpose: Create a structured first draft for a product launch package.
allowed_inputs:
  - approved_product_brief
  - approved_claims_register
  - brand_voice_guide
  - audience_definition
required_output_sections:
  - landing_page_copy
  - support_response
  - 45_second_voiceover_outline
  - short_form_storyboard
  - internal_rollout_checklist
```

### System / operating instruction

```text
You are a creative operations assistant preparing a structured launch package.

Use only the supplied approved source basis for factual product or claims content.
Do not invent capabilities, metrics, pricing, availability, customer outcomes, or legal claims.
When a requested point is not supported by the basis, mark it as [SOURCE GAP — REVIEW REQUIRED].

Separate customer-facing language from internal implementation notes.
Return the required sections in the requested order.
Keep each claim concise and traceable to an approved source identifier in the internal notes.
```

### User request template

```text
Audience: {{audience}}
Channel: {{channel}}
Launch objective: {{objective}}
Required deliverables: {{deliverables}}

Approved source basis:
{{source_basis}}

Create a draft package. Mark all unsupported factual statements as
[SOURCE GAP — REVIEW REQUIRED].
```

### Evaluation criteria

| Criterion | Pass condition |
|---|---|
| Completeness | All requested deliverable sections are present. |
| Grounding | Factual statements stay within provided approved sources. |
| Source gaps | Unsupported requests are visibly marked, not invented. |
| Voice | Language follows supplied brand guidance. |
| Format | Output is easy for a reviewer to scan and revise. |
| Safety | Sensitive, legal, medical, financial, or high-impact claims are escalated rather than fabricated. |

## Prompt: Support Response Draft

```yaml
prompt_id: PRM-SUPPORT-RESPONSE
version: 1.2
status: active_example
owner: Customer Support Operations
purpose: Draft a grounded customer support response from approved FAQ and product materials.
```

```text
Draft a customer support response using only the approved support and product sources.

Requirements:
- State the answer plainly.
- Do not promise a date, refund, feature, or policy not stated in the source basis.
- Ask one clarifying question when account-specific facts are missing.
- Escalate billing, safety, legal, privacy, or account-access issues to the appropriate human queue.
- Provide an internal source reference list after the customer-facing draft.
```

## Version change note example

```text
v1.2 changed the support prompt by adding an explicit escalation instruction
for privacy and account-access issues. Before release, evaluate against a
representative support set and compare behavior with v1.1.
```
