# Safe Evaluation Boundary

This repository is a public, bounded evaluation artifact created by **Samantha Revita** for demonstrating operational intelligence and practical AI Specialist capability.

## What this repository is

- A browser-only interactive consequence surface.
- A deterministic public evaluation harness with tasks, graders, schemas, sample runs, and tests.
- A set of architecture notes and implementation examples for source authority, lineage, resolution, witness, reviewed standing, revalidation, and replay.

## What this repository is not

This repository is **not**:

- a production deployment;
- a hosted AI service;
- a claim of active integration with a named third-party provider;
- a multi-tenant application;
- a customer data environment;
- a source for credentials, API keys, tokens, training data, or confidential materials;
- a complete private runtime or release of protected implementation details.

## Public simulation boundary

The browser surface and the deterministic runner are intentionally bounded:

```text
no API keys
no external model calls
no customer data
no server-side database
no browser telemetry
no cryptographic production attestation
```

Witness IDs and receipt values are local demonstration markers. They show visible state and replay design; they must not be treated as production evidence.

## Deterministic refusal conditions

The public grader does not convert absent evidence into permission. Its failure-closed conditions are defined in [`graders/basic.py`](./graders/basic.py):

| Refusal constant | Trigger |
|---|---|
| `REFUSE_REASON_MISSING_MATERIAL_BASIS` | No material basis is present. |
| `REFUSE_REASON_AMBIGUOUS_AUTHORITY` | Material is inactive, lacks authority, or does not permit the intended use. |
| `REFUSE_REASON_MISSING_LINEAGE` | Prompt lineage or provider route is absent. |
| `REFUSE_REASON_UNBOUNDED_RESOLUTION` | Resolution state or reason is not explicit. |
| `REFUSE_REASON_MISSING_WITNESS` | A `MAY_BIND` result lacks a witness. |
| `REFUSE_REASON_UNREVIEWED_STANDING` | A claimed reviewed standing lacks a named reviewer. |
| `REFUSE_REASON_MATERIAL_DRIFT` | Material drift occurs without `REVALIDATION_REQUIRED`. |
| `REFUSE_REASON_MISSING_REPLAY` | No replay trace exists. |

These conditions are exercised in [`tests/test_basic_grader.py`](./tests/test_basic_grader.py) and illustrated in [`samples/runs/run_003_agent.json`](./samples/runs/run_003_agent.json).

## Intellectual-property boundary

The public materials explain visible workflow patterns and safe evaluation examples. They do not grant rights to private systems, protected research, internal implementation, confidential designs, customer work, or materials not explicitly included in this repository.

All rights not expressly granted are reserved by Samantha Revita.

## Responsible use

Use this repository to assess approach, clarity, interface design, implementation judgment, and operational consequence reasoning. Do not use it as the basis for handling sensitive data, making automated high-impact decisions, or representing a production assurance process without appropriate engineering, security, legal, and domain review.
