# UASEP Task Lifecycle

This document defines the canonical lifecycle for work performed by chat-based agents through connected repository tools.

## 1. Discover

Read `AGENTS.md`, resolve the applicable protocol, inspect `.uasep/state/`, and identify the active branch and available capabilities.

## 2. Define

Create or select a task with:

- objective;
- scope and write set;
- dependencies;
- owner;
- acceptance criteria;
- risk level;
- verification plan.

A task without enough information to execute safely is `BLOCKED` or `UNKNOWN`, not implicitly ready.

## 3. Analyze

Inspect the actual repository and recent history. Classify the task relative to other active work as `INDEPENDENT`, `DEPENDENT`, `CONFLICTING`, or `BLOCKED`.

## 4. Claim

Record ownership before consequential edits. The claimed write set must be explicit enough to detect collisions with other agents.

## 5. Execute

Apply only changes within the approved scope. Independent tasks may be executed in the same batch. Conflicting or dependent tasks are serialized or explicitly coordinated.

## 6. Verify

Run the strongest verification available for the risk level. Separate:

- implementation evidence;
- verification evidence;
- remaining unknowns.

Use `VERIFIED`, `PARTIALLY_VERIFIED`, `UNKNOWN`, or `FAILED` honestly.

## 7. Record

Update durable state with the result, changed files, evidence, decisions, failures, and any blockers. A chat message is not a durable record.

## 8. Handoff

Leave the repository in a continuable state. `HANDOFF.md` must identify the current objective, task, completed work, unverified work, blockers, relevant decisions, and exact next action.

## 9. Complete

Mark `DONE` only when acceptance criteria are satisfied and sufficient evidence is recorded. Otherwise retain the appropriate non-terminal status.

## Recovery

After interruption, start from durable state rather than reconstructing work from memory. Re-check ownership and repository contents before continuing. Stale claims must be released or reconciled before edits resume.
