# Self-Improvement Loop

Extends `SELF_MAINTENANCE.md`.

## Loop

`MEASURE → FIND WASTE → TASK → FIX → VERIFY → RECORD`

Signals (see `runtime/metrics.py`):

- high retries / stagnation
- duplicated work
- weak acceptance checks
- version drift (`runtime/drift.py`)

## Restraint

Protocol core changes require versioning, evidence, and rollback. Prefer PATCH/MINOR improvements over silent MAJOR behavior changes.
