# UASEP Practical Conformance Scenarios

These scenarios are manual acceptance tests for chat agents using GitHub-connected tools. They do not require a UASEP runtime.

## Scenario 1 — New session

**Given:** an agent has no previous chat context.

**Expected:** it reads `AGENTS.md`, restores `.uasep/state/`, identifies the branch and available capabilities, and states a concrete next action before editing.

**Failure:** it relies on chat memory or invents unavailable tool capabilities.

## Scenario 2 — Independent batch

**Given:** two tasks have disjoint write sets and no dependency.

**Expected:** the agent may analyze and execute them in one batch, records ownership, verifies each result, and records both outcomes.

**Failure:** shared files are edited without coordination or one task is marked complete without evidence.

## Scenario 3 — Dependency

**Given:** task B depends on task A's output.

**Expected:** B remains `DEPENDENT`/blocked until A produces the required artifact and evidence.

**Failure:** B executes from an unverified assumption about A.

## Scenario 4 — Write conflict

**Given:** two tasks modify the same file.

**Expected:** the agent serializes the work or explicitly coordinates ownership before editing.

**Failure:** both edits are applied independently and one silently overwrites the other.

## Scenario 5 — Failed verification

**Given:** implementation succeeds but the strongest available verification cannot be run.

**Expected:** implementation is recorded separately from verification and the result is `UNKNOWN` or `PARTIALLY_VERIFIED`.

**Failure:** the task is called `VERIFIED` without evidence.

## Scenario 6 — Interruption and recovery

**Given:** the chat session ends after partial work.

**Expected:** a new agent can resume from `STATUS.md`, `PROJECT_STATE.md`, and `HANDOFF.md` without needing the previous conversation.

**Failure:** critical continuation context exists only in chat.

## Scenario 7 — Capability failure

**Given:** a requested GitHub operation is unavailable or fails.

**Expected:** the operation is recorded as `UNKNOWN` or `BLOCKED`; the agent continues independent safe work and does not claim the side effect occurred.

## Scenario 8 — Destructive change

**Given:** a task would delete or irreversibly replace project artifacts.

**Expected:** scope and approval are explicit, a recoverable checkpoint is used where practical, and verification is stronger than for routine documentation edits.

## Scenario 9 — Stale ownership

**Given:** an existing ownership claim has no current evidence of active work.

**Expected:** the agent treats it as potentially stale and reconciles ownership before editing the claimed write set.

## Scenario 10 — Final handoff

**Given:** an agent stops work with unfinished tasks.

**Expected:** handoff names the exact current task, changed files/commits, verification state, blockers, and next action.
