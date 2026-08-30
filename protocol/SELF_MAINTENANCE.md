# Self-Maintenance and Self-Improvement

Once primary objectives are stable, UASEP continuously monitors the project and its engineering process.

## Maintenance loop

`MONITOR → DETECT → DIAGNOSE → TASK → FIX → TEST → REVIEW → INTEGRATE`

Look for regressions, dependency issues, security weaknesses, documentation drift, technical debt, flaky tests, stale automation, performance problems, and operational risks.

## Engineering-system improvement

Measure the development process itself:

- repeated failures
- duplicated work
- wasted execution
- weak tests
- recurring blockers
- poor task decomposition
- unnecessary manual steps

Create improvement tasks when evidence supports them.

## Restraint

Self-improvement must not become uncontrolled self-modification. Changes to core protocol behavior require versioning, evidence, review, and rollback capability.

## Documentation restraint

Every new document must trace to a concrete defect, drift finding, or acceptance requirement. Generated documentation that merely restates existing material under a new title is noise: it obscures the canonical tree, inflates review cost, and contradicts the smallest-safe-change rule.

- Prefer editing an existing canonical document over adding a new one.
- Speculative or supplemental material belongs in `docs/archive/` and is never normative.
- If a document cannot name the requirement it serves, do not write it.
- Do not manufacture documentation cycles merely to keep a maintenance queue busy.

## Protocol evolution

When a new protocol version is adopted, preserve project state and perform an explicit migration. Never silently discard incompatible state.
