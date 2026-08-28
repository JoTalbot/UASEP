# UASEP Backlog

Priority is dynamic. Re-score tasks using user value, dependency readiness, risk, reversibility, and available evidence.

## P0 — Foundations

- UASEP-PROTO-001: Complete repository-wide documentation audit for runtime/AIOS2 assumptions.
- UASEP-PROTO-002: Define canonical durable project status format.
- UASEP-PROTO-003: Define canonical evidence record format.
- UASEP-PROTO-004: Define agent ownership/lease format for parallel work.
- UASEP-PROTO-005: Define decision record format.
- UASEP-PROTO-006: Define explicit source-of-truth hierarchy.

## P1 — Agent workflow

- UASEP-AGENT-001: Document mandatory startup/restore procedure.
- UASEP-AGENT-002: Document task decomposition and acceptance criteria.
- UASEP-AGENT-003: Document large-batch parallel analysis and conflict-free execution.
- UASEP-AGENT-004: Document verification and evidence rules.
- UASEP-AGENT-005: Document failure recovery and anti-loop strategy.
- UASEP-AGENT-006: Document session handoff and continuation.
- UASEP-AGENT-007: Document multi-machine/multi-agent coordination.

## P1 — Chat + GitHub Connector

- UASEP-CONNECT-001: Define the standard ChatGPT/GitHub operating loop.
- UASEP-CONNECT-002: Define capability discovery and tool limitations.
- UASEP-CONNECT-003: Define safe commit/push behavior.
- UASEP-CONNECT-004: Define how agents report verified vs unknown results.
- UASEP-CONNECT-005: Define recovery when a connector action fails or is unavailable.

## P2 — Examples and adoption

- UASEP-EXAMPLE-001: New-project example.
- UASEP-EXAMPLE-002: Existing-project adoption example.
- UASEP-EXAMPLE-003: Parallel batch example.
- UASEP-EXAMPLE-004: Conflict/recovery example.
- UASEP-EXAMPLE-005: Handoff between agents on different machines.

## P2 — Quality

- UASEP-QUALITY-001: Documentation consistency self-audit.
- UASEP-QUALITY-002: Example-based conformance scenarios.
- UASEP-QUALITY-003: Protocol drift detection guidance.

## Non-goals

Runtime implementation, local daemon/CLI, executor framework, autonomous process supervisor, and AIOS2 integration are out of scope unless the project direction is explicitly changed.
