# UASEP Agent Contract

This repository is the durable coordination layer for AI agents working through chat and GitHub-connected tools. There is no UASEP runtime to install or execute.

## Before every task

1. Read this file.
2. Read the relevant `skills/` workflow.
3. Restore context from `.uasep/state/HANDOFF.md` and `.uasep/state/PROJECT_STATE.md`.
4. Read `.uasep/planning/BACKLOG.md` and the relevant master-plan section.
5. Inspect the actual repository and current branch/history.
6. Establish Agent Readiness using `protocol/AGENT_READINESS.md`.
7. Create or restore the applicable Task Contract using `protocol/TASK_CONTRACT.md`.
8. For multi-task work, create/restore a Batch Manifest using `protocol/BATCH_MANIFEST.md`.
9. Check active ownership and recent changes before touching shared files.

## Execution rules

- Work only on the branch explicitly assigned to you.
- Never overwrite or revert another active agent's work without a deliberate integration decision.
- Prefer independent tasks and large safe batches.
- Before parallel work, declare each task's write set and dependencies.
- Do not parallelize tasks with overlapping writes unless explicitly coordinated.
- Make small, logically atomic commits.
- Verify changes before claiming completion and record evidence using `protocol/EVIDENCE_SCHEMA.md`.
- Never fabricate tests, CI results, files, commits, tool access, or external actions.
- Treat the repository as the durable source of truth; chat is temporary context.

## Required task record

Every substantive task must have a Task Contract containing objective, scope/files, dependencies, conflicts, acceptance criteria, owner/agent, branch, risks, verification plan, result/evidence, and next action or blocker.

## Parallel batch protocol

1. Analyze up to the practical batch limit in parallel.
2. Create/update the Batch Manifest.
3. Classify tasks as independent, dependent, conflicting, or blocked.
4. Execute only independent/conflict-free work together.
5. Verify each result independently and record evidence.
6. Update state, evidence, and handoff.

## Failure and recovery

Record failures in `.uasep/knowledge/FAILURES.md`. Do not repeatedly retry an unchanged strategy. When blocked, state exactly what is missing and what can safely continue independently.

## Handoff

Before stopping, update `.uasep/state/HANDOFF.md` with the exact current step, completed work, unverified work, blockers, changed files/commits, and recommended next action.

## Definition of done

A task is done only when its acceptance criteria are satisfied and the result has evidence. If verification is unavailable, label the result `UNKNOWN`, not `VERIFIED`.
