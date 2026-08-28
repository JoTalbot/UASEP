# Batch Execution Guide

Use this procedure when a request contains many tasks.

## 1. Analyze together

For every task identify the exact files, write set, dependencies, conflicts, risk, acceptance criteria, and verification. Analysis may be parallel even when execution cannot be.

## 2. Partition execution

Put tasks with satisfied dependencies and non-overlapping write sets into the same execution group. Serialize dependent or conflicting work. Treat unavailable capabilities as `UNKNOWN` or `BLOCKED`, never as success.

## 3. Execute independently

Prefer atomic, reversible repository changes. Keep each task's write set narrow. Do not edit a file owned by another active task without explicit coordination.

## 4. Verify independently

Verify each task against its own acceptance criteria. Batch completion is not evidence that every task succeeded.

## 5. Persist

Update durable state, evidence, failures, and handoff artifacts with observed results. Include changed files and commit references when available.

## 6. Stop conditions

Stop or re-plan when a dependency fails, a write-set conflict appears, ownership is stale, or the available connector cannot perform a required operation. Record the limitation rather than looping.

## Example execution model

```text
Analyze H01-H20
        |
        +-- Group A: independent fixture/docs tasks
        |
        +-- Group B: tests depending on fixtures
        |
        +-- Group C: state/status synchronization
        |
        +-- External: fresh-agent acceptance
```

The protocol remains runtime-free; the batch is coordinated through repository state and the host agent's available tools.
