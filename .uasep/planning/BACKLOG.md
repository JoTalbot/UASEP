# UASEP Backlog

Priority is dynamic. Re-score tasks using user value, dependency readiness, risk, reversibility, and available evidence.

## P0 — Foundations

- [x] UASEP-PROTO-001: Complete repository-wide audit for runtime/AIOS2 assumptions. — active-tree migration complete; historical references are provenance only.
- [x] UASEP-PROTO-002: Define canonical durable project status format.
- [x] UASEP-PROTO-003: Define canonical evidence record format.
- [x] UASEP-PROTO-004: Define agent ownership/lease format for parallel work.
- [x] UASEP-PROTO-005: Define decision record format.
- [x] UASEP-PROTO-006: Define explicit source-of-truth hierarchy.

## P1 — Agent workflow

- [x] UASEP-AGENT-001: Document mandatory startup/restore procedure.
- [x] UASEP-AGENT-002: Document task decomposition and acceptance criteria.
- [x] UASEP-AGENT-003: Document large-batch parallel analysis and conflict-free execution.
- [x] UASEP-AGENT-004: Document verification and evidence rules.
- [x] UASEP-AGENT-005: Document failure recovery and anti-loop strategy.
- [x] UASEP-AGENT-006: Document session handoff and continuation.
- [x] UASEP-AGENT-007: Document multi-machine/multi-agent coordination.

## P1 — Chat + GitHub Connector

- [x] UASEP-CONNECT-001: Define the standard Chat + GitHub operating loop.
- [x] UASEP-CONNECT-002: Define capability discovery and connector/tool limitations.
- [x] UASEP-CONNECT-003: Define safe repository-update/commit behavior.
- [x] UASEP-CONNECT-004: Define how agents report verified vs unknown results.
- [x] UASEP-CONNECT-005: Define recovery when a connector action fails or is unavailable.

## P2 — Examples and adoption

- [x] UASEP-EXAMPLE-001: New-project example.
- [x] UASEP-EXAMPLE-002: Existing-project adoption example.
- [x] UASEP-EXAMPLE-003: Parallel batch example.
- [x] UASEP-EXAMPLE-004: Conflict/recovery example.
- [x] UASEP-EXAMPLE-005: Handoff between agents on different machines.

## P3 — Maintenance hygiene (2026-08-30)

- [x] UASEP-MAINT-M62: Repair canonical CI (restore checkout/setup-python), replace echo-only workflows with behavioral policy tests, minimize the workflow set to four, archive non-normative cycle documentation, remove orphaned root state files, add LICENSE/CODEOWNERS, and reconcile durable state. — evidence: `.uasep/evidence/EV-UASEP-MAINT-M62-2026-08-30.json`.

## P2 — Quality

- [x] UASEP-QUALITY-001: Documentation consistency self-audit — active-tree consistency rules documented; historical index results remain non-authoritative.
- [x] UASEP-QUALITY-002: Example-based conformance scenarios.
- [x] UASEP-QUALITY-003: Protocol drift detection guidance.

## Non-goals

Runtime implementation, local daemon/CLI, executor framework, autonomous process supervisor, and AIOS2 integration are out of scope unless the project direction is explicitly changed.

## Execution rule

Do not mark a task complete from intent alone. Record changed files, evidence, unresolved risks, and next action in `.uasep/state/STATUS.md` and `.uasep/state/HANDOFF.md`.
