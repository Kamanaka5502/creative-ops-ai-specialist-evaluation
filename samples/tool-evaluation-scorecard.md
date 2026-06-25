# AI Tool Evaluation Scorecard

Use this scorecard to evaluate a hosted provider, open-source model, creative tool, speech tool, retrieval component, or automation framework against a specific operational use case.

## Evaluation context

```text
Use case: ________________________________________________
Business owner: __________________________________________
Technical owner: _________________________________________
Data classification: ______________________________________
Target users: ____________________________________________
Decision date: ___________________________________________
```

## Scorecard

Score each category from 1 (unacceptable) to 5 (strong fit). Add evidence; do not score by impression alone.

| Category | Score | Evidence / questions |
|---|---:|---|
| Task fit |  | Does it solve the defined task better than the current workflow? |
| Output quality |  | Does it meet factual, style, structure, and task-completion requirements? |
| Grounding / retrieval fit |  | Can it use approved knowledge sources and signal unsupported content? |
| Data and IP boundary |  | Are retention, training, export, and access terms appropriate for the data? |
| Integration |  | Are API, SDK, auth, rate limits, webhooks, and failure modes workable? |
| Observability |  | Can the team record route, version, prompt, errors, latency, and outcome? |
| Reliability |  | How does it behave under timeout, quota, malformed input, or provider change? |
| Cost |  | Is cost predictable for expected use and peak volume? |
| Security |  | Can secrets, access, logs, and permissions be handled appropriately? |
| Human workflow |  | Does it improve the operator experience or create review burden? |
| Governance |  | Are escalation, review, release, and revalidation controls feasible? |
| Vendor maturity |  | Is support, documentation, roadmap, and continuity adequate? |

## Minimum evidence packet

```text
- documented use case and non-goals
- representative test inputs
- expected outputs and refusal cases
- quality examples and failures
- data-flow assessment
- cost and latency observations
- integration notes
- risk and review plan
- recommendation: adopt, adapt, defer, or reject
```

## Decision statement template

```text
Decision: [ADOPT / ADAPT / DEFER / REJECT]

Reason:
The tool is [or is not] a fit for [defined use case] because [evidence].

Operating conditions:
- approved data classification: ______
- required human review: ______
- permitted provider/model route: ______
- prompt/version controls: ______
- monitoring and change triggers: ______

Next step:
_______________________________________________
```

## Example interpretation

A tool can have excellent creative output and still be the wrong operational choice if data handling is unclear, integration is unreliable, cost is unpredictable, or review requirements cannot be met. Conversely, a tool with modest baseline capability may be a strong fit when wrapped with retrieval, structured prompts, review controls, and workflow automation.
