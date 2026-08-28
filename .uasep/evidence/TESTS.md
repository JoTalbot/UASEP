# Test Evidence

Executable runtime tests live under `tests/`.

## Evidence policy

Record date, task, command/check, result, environment, and relevant artifact/commit. Distinguish verified execution from static inspection.

## Current verification

- Date: 2026-08-28
- Task: Align cycle-budget contract; restore green local suite
- Command: `python -m pytest -q`
- Result: 103 passed
- Environment: Python 3.10, local sandbox
- Status: VERIFIED locally; CI pending observation of the 3.1.1 workflow run
- Branch: `main`
- Note: GitHub Actions status must be observed before claiming a verified CI pass.
