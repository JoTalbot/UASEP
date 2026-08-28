# Skill: Parallel Batch

Use when several tasks may be progressed in the same turn.

## Task matrix

For every candidate task record: ID, objective, files/write set, dependencies, owner, risk, acceptance criteria, and tests/verification.

## Classification

- **Independent**: no dependency and no overlapping write set.
- **Dependent**: must wait for another task.
- **Conflicting**: overlapping writes or incompatible assumptions.
- **Blocked**: missing information, authority, or required capability.

Only independent tasks should be executed together without coordination.

## Batch sequence

1. Analyze the maximum practical number of tasks.
2. Group independent tasks.
3. Execute them without cross-contaminating scope.
4. Verify each task.
5. Integrate and inspect the combined result.
6. Persist evidence and handoff.

A failed task must not invalidate unrelated completed tasks. Do not hide a blocker by marking it complete.
