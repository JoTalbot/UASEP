# UASEP Conformance Specification

Version: 3.3

## Purpose

UASEP is a repository-native operating protocol for AI agents working through chat and connected repository tools. Conformance describes agent behavior and durable project artifacts; it does not require a UASEP runtime.

## Required agent behavior

A conformant agent MUST:

1. Discover the actual repository, assigned branch, available tools, and applicable instructions before consequential work.
2. Restore context from `.uasep/state/` before acting; chat history is not the source of truth.
3. Represent meaningful work as tasks with objective, scope, dependencies, acceptance criteria, owner, risk, write set, and verification plan.
4. Inspect actual files and recent history before proposing or applying changes.
5. Use only capabilities actually available in the current session; never assume a connector action exists.
6. Classify candidate tasks as independent, dependent, conflicting, or blocked before batch execution.
7. Execute tasks in parallel only when dependencies and write sets are compatible and ownership is explicit.
8. Verify consequential changes with evidence proportional to risk and distinguish implementation from verification.
9. Persist status, decisions, failures, evidence, and handoff information in repository artifacts.
10. Detect repeated failures, no-op progress, stale ownership, and conflicting edits; change strategy or stop safely.
11. Distinguish `VERIFIED`, `PARTIALLY_VERIFIED`, `UNKNOWN`, and `FAILED` claims.
12. Protect destructive or irreversible operations with explicit approval and a recoverable checkpoint where practical.
13. Leave the repository understandable and continuable by an agent with no previous chat context.
14. Never claim a tool action, test, CI result, commit, push, review, or external effect without evidence.
15. Before editing a consequential scope, establish an explicit ownership claim; overlapping active claims MUST be coordinated or serialized.
16. Treat ownership as a lease: refresh, release, transfer, or reconcile stale claims in durable state rather than silently taking over.

## Durable artifacts

The canonical operational artifacts are:

- `AGENTS.md` — mandatory agent contract.
- `skills/` — reusable workflows.
- `.uasep/state/STATUS.md` — compact current status.
- `.uasep/state/PROJECT_STATE.md` — durable project state and constraints.
- `.uasep/state/HANDOFF.md` — continuation context.
- `.uasep/planning/` — backlog and plan.
- `.uasep/knowledge/` — decisions, discoveries, failures, lessons.
- `.uasep/evidence/` — verification records.
- `protocol/` — normative rules.

## Completion invariant

A task MUST NOT be marked `DONE` solely because an implementation attempt was made. Acceptance criteria must be satisfied and evidence recorded. If evidence is unavailable, use `UNKNOWN` rather than implying success.

## Recovery invariant

After interruption, durable artifacts MUST identify the current objective, task, completed work, unverified work, blockers, relevant decisions, changed files/commits, and next action.

## Parallel-work invariant

Tasks may be analyzed in parallel, but execution may be parallel only when their dependencies and write sets are compatible. Conflicting work requires explicit coordination or serialization.

## Ownership invariant

An active ownership claim MUST identify the task, owner/session, branch, write set, claim time, and expected review/completion point. Stale or overlapping claims require explicit reconciliation before consequential edits.

## Connector invariant

GitHub-connected tools are capabilities of the current agent session, not protocol guarantees. A missing or failed connector action is recorded as `UNKNOWN` or `BLOCKED` as appropriate; it is never silently treated as success.

## Portability invariant

UASEP state and instructions MUST remain understandable through ordinary repository files and MUST NOT depend on hidden chat history, a specific AI vendor, or an executable UASEP runtime.
