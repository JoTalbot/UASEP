# Failed Approaches

## Cycle budget overwrote verified terminal phase

- Symptom: `run_until_blocked(..., max_cycles=1)` completed a task, then rewrote `phase` from `verified` to `blocked` with `cycle budget exhausted`.
- Root cause: budget exhaustion ran after every loop exit, including when no remaining work existed.
- Failed approach: treating `verified` as a non-terminal mid-cycle status that the budget could always preempt.
- Resolution: if no incomplete tasks remain, keep the verified/maintenance phase; only block when work is still outstanding. A later budgeted run may drop a previous `cycle budget exhausted` blocker and continue.
- Tests: `test_verified_terminal_phase_survives_cycle_budget`, `test_run_until_blocked_marks_unresolved_retry_as_blocked`.

## Hardening tests assumed a different retry vocabulary

- Symptom: `Task(..., max_attempts=, attempts=)` TypeError; first failure expected `phase == "blocked"` with `current_task` still set.
- Root cause: tests were written against an unshipped API. Established contract is `failure_count` + `retrying` then `blocked` after `max_failures`.
- Resolution: keep the established supervisor contract; align hardening tests to it. Do not silently rename retry fields.
