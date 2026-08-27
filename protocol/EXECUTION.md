# Execution Protocol

## Start

1. Discover environment and capabilities.
2. Locate project root.
3. Load project instructions and UASEP state.
4. If state is missing, initialize it from observed reality.
5. Audit before substantial changes.

## Planning

Represent meaningful work as tasks with:

- objective
- acceptance criteria
- dependencies
- priority
- risk
- owner/agent
- status
- evidence

Prefer a dependency-aware task graph over a flat checklist.

## Execution

For each task:

`UNDERSTAND → CHANGE → TEST → REVIEW → VERIFY → PERSIST`

Parallelize only independent work. Protect shared artifacts from conflicting concurrent writes.

## Recovery

On failure:

1. Capture exact failure evidence.
2. Identify root cause.
3. Avoid repeating an identical failed approach.
4. Try a materially different safe approach.
5. After repeated failure, perform architectural review.
6. Escalate only when genuinely blocked.

## Anti-loop

Detect repeated identical failures, no-op iterations, and stagnation. Stop the current approach and re-plan rather than endlessly patching symptoms.

## Handoff

Before session termination, persist current task, changes, tests, blockers, decisions, and the next best action.
