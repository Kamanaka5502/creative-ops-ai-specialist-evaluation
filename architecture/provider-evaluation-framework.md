# Provider and Tool Evaluation Framework

## Objective

AI tool adoption should be evaluated as an operational decision, not only a feature comparison. The right provider or open-source component depends on the use case, data classification, quality threshold, integration effort, reliability needs, cost model, and ability to observe or control behavior.

## Evaluation dimensions

| Dimension | Questions to answer |
|---|---|
| Task fit | What exact task will the tool improve? What should it not be used for? |
| Output quality | What quality threshold is required? How will it be measured? |
| Grounding | Can the workflow constrain output to approved material when needed? |
| Data / IP | What data is sent, stored, retained, or used for training? |
| Integration | Are APIs, SDKs, auth, webhooks, and rate limits viable for the intended workflow? |
| Reliability | What happens during timeout, provider error, quota limit, or model change? |
| Observability | Can the team record model, prompt version, route, error, latency, and outcome? |
| Cost | What is the unit cost, peak-load cost, and likely budget guardrail? |
| Security | What access control, secret handling, logging, and vendor-review requirements apply? |
| Governance | What review, human escalation, and release rules are required? |
| Change management | How will model/provider changes be evaluated before wider rollout? |

## Evaluation sequence

```text
1. Define the job to be done.
2. Establish success and refusal criteria.
3. Classify data and risk.
4. Identify candidate tools or models.
5. Run a bounded proof of concept with representative examples.
6. Measure quality, latency, cost, failure behavior, and operator usability.
7. Decide: adopt, adapt, defer, or reject.
8. Document operating conditions and rollout controls.
9. Monitor change, incidents, and drift after launch.
```

## Provider route model

A workflow should make route selection explicit where it materially affects behavior.

```yaml
route_id: creative-evaluation-route
provider_category: hosted_language_model
mode: dry_run_or_sandbox
data_classification: no_customer_data
prompt_registry: required
source_basis: required_for_grounded_tasks
human_review: required_for_external_release
fallback: hold_and_escalate
observability: prompt_version + provider_route + outcome + timestamp
```

## Named provider categories

Teams may evaluate hosted language-model providers, image/video generation tools, speech tools, embedding/search services, open-source models, fine-tuning platforms, and orchestration systems. Tools such as OpenAI, Runway, ElevenLabs, and comparable services should be evaluated against the same operating criteria rather than adopted solely on novelty.

This repository does **not** claim active integrations with any named provider. It demonstrates the decision framework and workflow controls that should surround such integrations.

## Example decision outcomes

| Outcome | Meaning |
|---|---|
| Adopt | Tool meets a defined use case with acceptable quality, boundaries, cost, and controls. |
| Adapt | Tool is viable but requires wrappers, retrieval, review, or workflow changes. |
| Defer | Value may exist, but timing, data readiness, reliability, or ownership is insufficient. |
| Reject | Tool does not meet task, data, security, cost, or governance requirements. |

## Continuous evaluation

Provider evaluation is not one-time. Re-run targeted evaluation when there is a material change in:

- model or model family;
- API behavior, pricing, retention policy, or feature set;
- data classification or business use case;
- prompt or retrieval design;
- incident history;
- regulation, contract, or policy.

See `samples/tool-evaluation-scorecard.md` for a reusable scorecard.
