# UASEP Task Contract

Every consequential task MUST have a durable contract before execution.

## Required fields

- `id`: unique stable task identifier.
- `objective`: one-sentence intended outcome.
- `owner`: current agent/session identifier.
- `branch`: exact branch being modified.
- `write_set`: files or bounded directories the task may change.
- `dependencies`: task IDs or explicit `NONE`.
- `conflicts`: known overlapping scopes or explicit `NONE`.
- `acceptance`: observable completion criteria.
- `risk`: `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`.
- `verification`: planned checks and evidence required.
- `status`: lifecycle status.

## Status

Use `READY`, `IN_PROGRESS`, `BLOCKED`, `UNKNOWN`, `PARTIALLY_VERIFIED`, `VERIFIED`, `FAILED`, or `DONE` according to the lifecycle and evidence rules.

`DONE` requires satisfied acceptance criteria and recorded evidence. `VERIFIED` describes verification evidence; it does not by itself imply all administrative closure is complete.

## Scope rule

The write set is an authorization boundary, not a suggestion. Discovered work outside it becomes a new task or requires an explicit contract update and ownership reconciliation.

## Minimal template

```text
ID: UASEP-TASK-XXX
OBJECTIVE: ...
OWNER: ...
BRANCH: ...
WRITE_SET: ...
DEPENDENCIES: NONE
CONFLICTS: NONE
ACCEPTANCE:
- ...
RISK: LOW
VERIFICATION:
- ...
STATUS: READY
```
