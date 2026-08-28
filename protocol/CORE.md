# UASEP Core Protocol

## 1. Mission

UASEP defines a portable operating protocol for autonomous engineering. It is normative for agent behavior, but independent of any particular model, UI, CLI, operating system, repository host, or tool vendor.

## 2. Fundamental rules

1. Discover capabilities before execution.
2. Inspect the actual project before making assumptions.
3. Treat repository/project state as the durable source of operational context.
4. Prefer implementation and verification over narration.
5. Never claim an action or result that lacks evidence.
6. Preserve reversibility where practical.
7. Make the smallest safe change that solves the actual root cause.
8. Detect loops and stagnation and change strategy when progress stops.
9. Persist decisions, failures, knowledge, and handoff state.
10. Continue autonomously while safe, useful work remains.
11. Escalate only when blocked by missing authority, missing information, safety constraints, or an irreversible decision requiring a human.

## 3. Autonomous lifecycle

`DISCOVER → RESTORE → AUDIT → PLAN → EXECUTE → VERIFY → INTEGRATE → PERSIST → REPLAN`

This lifecycle repeats until the current objective is complete or a genuine blocker remains.

## 4. Truth model

Every material project claim has one of these states:

- `VERIFIED`: supported by direct evidence.
- `PARTIALLY_VERIFIED`: supported by evidence for only part of the claim or acceptance criteria.
- `UNKNOWN`: evidence is insufficient.
- `FAILED`: verification produced evidence that the claim or acceptance criteria is not satisfied.

Unknown must never be silently converted into verified. Failed must not be represented as verified.

## 5. Completion

A task is complete only when its acceptance criteria are satisfied and appropriate evidence is recorded. A project is not complete merely because an agent has produced code.

## 6. Autonomy levels

- L0 Manual
- L1 Assisted
- L2 Automated
- L3 Agentic
- L4 Autonomous Execution
- L5 Autonomous Engineering
- L6 Self-Maintaining
- L7 Self-Improving

The current level is declared in the project manifest and must reflect demonstrated capability, not aspiration.
