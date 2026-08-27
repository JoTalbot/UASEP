# Decisions

## ADR-001 — Short bootstrap, full protocol in repository

Decision: Keep the user-facing bootstrap prompt short. Load normative behavior from UASEP and project-local state.

Reason: portability across ChatGPT, local CLIs, sandboxes, IDE agents, and future runtimes.

## ADR-002 — Capability discovery first

Decision: Never assume tool availability.

Reason: the same bootstrap must adapt to materially different environments.

## ADR-003 — Repository-backed state

Decision: Persist operational state in the project when external memory cannot be guaranteed.

Reason: session independence and reliable handoff.

## ADR-004 — Evidence-based completion

Decision: completion claims require evidence proportional to risk.

Reason: prevents false confidence and unverifiable status reporting.
