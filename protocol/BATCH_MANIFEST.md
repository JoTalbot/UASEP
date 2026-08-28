# UASEP Batch Manifest

A batch manifest describes work that is analyzed together and separates safe parallel execution from dependencies and conflicts.

## Required fields

- `batch_id`
- `objective`
- `tasks`
- `analysis_status`
- `execution_groups`
- `verification_plan`
- `owner`

Each task entry MUST reference a task contract.

## Analysis

For every task determine:

- dependencies;
- write set;
- conflicts;
- risk;
- verification requirements;
- execution eligibility.

Classify each task as `INDEPENDENT`, `DEPENDENT`, `CONFLICTING`, or `BLOCKED`.

## Execution groups

Tasks may share an execution group only when their dependencies are satisfied and their write sets are non-overlapping or explicitly coordinated. Dependent tasks move to a later group. Conflicting tasks are serialized or coordinated.

Example:

```text
BATCH-042
G1: T01 T02 T05
G2: T03 (depends:T01)
G3: T04 (conflicts:T02)
```

## Verification

Verification is recorded per task, not inferred from batch completion. One failed or blocked task does not automatically invalidate unrelated completed tasks, but the batch summary MUST expose every non-success state.

## Recovery

After interruption, rebuild the manifest from durable task/state records and actual repository contents. Never assume an entire group completed because the chat ended after the group started.
