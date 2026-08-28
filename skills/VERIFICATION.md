# Skill: Verification

Verification is a separate phase from implementation.

## Evidence levels

- `VERIFIED`: directly observed through an appropriate test, review, CI result, or repository inspection.
- `INFERRED`: derived from available evidence but not directly tested.
- `UNKNOWN`: insufficient evidence.
- `BLOCKED`: verification cannot currently be performed.

## Rules

- Inspect the final diff.
- Verify acceptance criteria, not merely syntax.
- Prefer project-native checks when available.
- Record the exact command/check/result when known.
- Never claim a CI run, test, review, push, or deployment that did not actually occur.
- If verification is unavailable, preserve that uncertainty in state and handoff.
