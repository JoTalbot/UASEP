# Parallel Batch Example

This example shows how a chat agent should handle several independent tasks through GitHub-connected tools.

## Input

A project needs four changes:

- A: update API documentation in `docs/api.md`;
- B: add a troubleshooting guide in `docs/troubleshooting.md`;
- C: add an architecture decision record in `docs/decisions/`;
- D: update an example in `examples/basic/`.

## Analysis

The tasks are independent when they have no cross-file dependency and their write sets do not overlap. The agent records four task IDs, owners/write sets, acceptance criteria, risks, and verification plans.

## Execution

A, B, C, and D may be executed in the same logical batch. Each change remains inside its declared write set. If any task discovers a dependency or collision, that task is paused and reclassified rather than silently modifying another task's scope.

## Verification

Verify each changed artifact independently. Record the actual changed files and evidence. A documentation update that can be inspected may be `VERIFIED` after inspection; a claimed external side effect without tool evidence remains `UNKNOWN`.

## Durable record

Update `.uasep/state/STATUS.md` and `.uasep/state/HANDOFF.md` with:

- batch/task IDs;
- completed and incomplete tasks;
- changed files/commits;
- verification state;
- unresolved risks;
- blockers;
- next action.

## Recovery

If the session ends mid-batch, another agent reads durable state, checks current repository contents and ownership, and resumes only unfinished tasks. It does not infer completion from the previous chat.
