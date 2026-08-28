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

## ADR-005 — Runtime-free reference protocol

Decision: UASEP's reference form is repository-native instructions, skills, state, evidence, tasks, decisions, and examples. No runtime, daemon, CLI, executor framework, or AIOS2 integration is required.

Reason: the primary operating environment is chat with a GitHub-connected agent. Adding executable infrastructure would create complexity without improving that workflow.

## ADR-006 — Durable status is mandatory

Decision: `.uasep/state/STATUS.md` is the compact operational handoff for substantive work.

Reason: another agent must be able to continue from repository state without hidden chat history.
