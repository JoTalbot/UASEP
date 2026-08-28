# UASEP Adoption Example

This example describes adopting UASEP in an existing repository without adding a runtime.

## Step 1 — Inspect

The agent reads the existing repository instructions and identifies the project branch, structure, active work, and available GitHub-connected capabilities.

## Step 2 — Add the protocol layer

Add or adapt:

- `AGENTS.md` for the mandatory agent contract;
- `skills/` for reusable workflows;
- `.uasep/state/` for durable status and handoff;
- `.uasep/planning/` for backlog and plans;
- `.uasep/knowledge/` for decisions/discoveries;
- `.uasep/evidence/` for verification records;
- `protocol/` for normative rules.

Do not add executable UASEP infrastructure.

## Step 3 — Establish baseline

Record the current objective, constraints, branch, known risks, existing CI/test status, and first actionable task in durable state. Do not rewrite unrelated project history merely to introduce UASEP.

## Step 4 — First task

Create a task contract with objective, scope/write set, dependencies, owner, acceptance criteria, risks, and verification plan. Claim ownership before consequential edits.

## Step 5 — Operate

Use the canonical lifecycle: discover → define → analyze → claim → execute → verify → record → handoff → complete.

Independent tasks can share a batch when their write sets and dependencies are compatible. Conflicting work is coordinated or serialized.

## Step 6 — Verify adoption

A fresh chat agent should be able to open the repository, read the durable state, identify the active task and branch, understand applicable rules, and continue without access to the previous conversation.

## Acceptance criteria

Adoption is complete when:

- the repository contains the required protocol/state artifacts;
- no UASEP runtime is required;
- current work has an explicit task and ownership model;
- verification/evidence rules are usable;
- handoff is sufficient for a fresh agent;
- project-specific rules remain intact and take precedence where compatible with core safety/integrity requirements.
