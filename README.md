# Creative Ops AI Specialist Evaluation

**Created by Samantha Revita**  
**Public evaluation build for AI workflow, RAG, prompt systems, provider evaluation, automation, and responsible release design.**

This repository is a bounded public demonstration of how I approach practical AI Specialist work: converting AI capability into reviewable, usable workflows with clear source grounding, version-aware prompts, explicit provider routes, operational controls, and evidence of what changed.

It is intentionally designed for technical reviewers, hiring teams, and cross-functional stakeholders who need to assess both implementation judgment and operating-model judgment.

## Start here

### Interactive evaluator sandbox

Open `index.html` locally in a browser, or serve this repository from a simple local static server:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

The sandbox lets a reviewer:

```text
edit a proposed movement
→ toggle temporary source-basis records
→ choose prompt lineage and a simulated provider route
→ resolve a boundary state
→ emit a witness
→ bind a reviewed standing
→ introduce material drift
→ inspect a local replay trace
```

### Architecture and implementation materials

| Area | Evidence |
|---|---|
| AI workflow prototyping | `architecture/workflow-architecture.md` and the interactive sandbox |
| RAG/document preparation | `architecture/rag-document-standards.md` and `samples/source-basis-example.json` |
| Prompt systems and versioning | `architecture/prompt-lineage-and-versioning.md` and `samples/prompt-library-example.md` |
| Provider evaluation | `architecture/provider-evaluation-framework.md` and `samples/tool-evaluation-scorecard.md` |
| Responsible AI release controls | `architecture/responsible-ai-release-controls.md` |
| LoRA adaptation approach | `architecture/lora-adaptation-approach.md` |
| Lightweight automation | `samples/automation_workflow_example.py` |

## What this demonstrates

### 1. Practical AI workflow design

AI capability is most useful when it becomes an understandable operating process rather than an isolated prompt. The included workflow model makes the operational sequence visible:

```text
intake
→ approved source basis
→ prompt lineage
→ provider route
→ output evaluation
→ witness / evidence record
→ human review
→ release standing
→ source or policy change
→ revalidation
→ replay / audit
```

### 2. RAG-ready document discipline

The repository shows a metadata-first approach to AI knowledge inputs: document identity, owner, version, approval standing, content type, provenance, update status, and retrieval fitness all matter before a document is allowed to influence an operational answer.

### 3. Prompt and provider visibility

Prompts are treated as managed operational artifacts rather than invisible instructions. Provider choice is also surfaced as a visible condition, because model, mode, data handling, quality, latency, and cost materially affect a workflow decision.

### 4. Responsible production use

A generated output is not automatically ready for release. This build demonstrates the distinction between:

```text
an output exists
```

and:

```text
an output has sufficient basis, stated conditions, review standing,
and evidence to be used operationally.
```

### 5. Lightweight implementation

The interactive sandbox is browser-only by design. The accompanying Python sample demonstrates a compact, testable pattern for source-basis evaluation and witness creation without requiring keys, customer data, or external services.

## Alignment to an AI Specialist role

This package is built to demonstrate capability across:

- identifying and prototyping AI opportunities for creative, technical, and operational teams;
- preparing and maintaining RAG-ready document knowledge structures;
- developing prompt libraries, automation patterns, and lightweight interfaces;
- evaluating commercial and open-source AI tools for task fit, risk, cost, data boundaries, and production readiness;
- supporting responsible AI use through review gates, provenance, versioning, revalidation, and traceability;
- translating experimental AI concepts into clear operational workflows that stakeholders can evaluate and use.

## Scope and safety boundary

This public repository contains only safe, illustrative materials.

It does **not** include:

- API keys, credentials, tokens, or secrets;
- customer or confidential data;
- external provider calls;
- a deployed multi-tenant application;
- protected implementation details from private work;
- claims that any specific third-party provider integration is active in this repository.

The interactive sandbox is a **simulation**. It is intended to demonstrate workflow and governance reasoning, interface design, and implementation patterns. See `SAFE_EVALUATION_BOUNDARY.md` for the full boundary.

## Author

**Samantha Revita**  
Creative Ops AI Workflow Studio  
GitHub: https://github.com/Kamanaka5502
