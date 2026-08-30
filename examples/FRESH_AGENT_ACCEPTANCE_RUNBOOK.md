# Fresh-Agent Acceptance Runbook

Batch: UASEP-HARDEN-2026-08-28
Branch: main

## Preconditions

- Use a genuinely fresh agent/session.
- Give the agent repository access only; do not provide originating chat history.
- Start from the current `main` tree.
- Use a neutral request: `Continue work on this repository.`

## Required observations

Record whether the fresh agent can independently identify:

1. repository and assigned branch;
2. `AGENTS.md` and the session bootstrap skill;
3. durable project state;
4. readiness and available capabilities;
5. current task and next action;
6. recent history and relevant files;
7. ownership and blockers;
8. applicable task, batch, and evidence rules.

## Acceptance assertions

The agent must determine from repository state alone that:

- UASEP is runtime-free;
- the protocol version matches `VERSION` (3.5.0);
- the project is in the adopted/documentation-first phase;
- no unrequested runtime implementation should be introduced;
- unverified CI/fresh-agent checks remain unverified until actually observed;
- the next action must respect scope, ownership, and verification constraints.

## Evidence

After the fresh session completes, create an evidence record using `protocol/EVIDENCE_SCHEMA.md` containing the tested commit/tree, agent/session identifier, operation, observed bootstrap behavior, result classification, and limitations.

Do not pre-fill a `VERIFIED` result. Until the test is actually executed by a fresh session, the acceptance status remains `NOT_RUN`/`UNKNOWN`.

## Safety

This runbook is procedural only. It does not grant additional write permissions, alter ownership, or authorize runtime implementation.
