# Changelog

## 3.1.3 — Runtime graph and checkpoint hardening

- Hardened checkpoint persistence with validation and atomic writes.
- Strengthened task graph validation coverage for safer execution planning.
- Added runtime consistency improvements for recovery-oriented workflows.
- Regression coverage expanded for state integrity and execution safety.
- Added checkpoint recovery regression tests for invalid data and restored state.

- CI validation trigger completed after hardening audit.
- CI verification retriggered after workflow audit.

## 3.1.2 — Persist per-task retry state for cold resume

- ProjectState and StateStore now persist `task_failures` so failure counts survive process restart (UASEP-RUNTIME-005).
- Supervisor restores failure counts on load and writes them on each failure.
- Integration test adjusted for shared-root state semantics under cold resume.
- Local pytest: 104 passed.

## 3.1.1 — Runtime verification and cycle-budget contract

- Supervisor no longer overwrites a verified terminal phase when the cycle budget ends with no remaining work.
- A new cycle budget may resume past a previous `cycle budget exhausted` block without dropping completed work.
- Hardening tests now match the established retry contract (`retrying` then `verified` / `blocked`).
- Local pytest: 103 passed.

## 3.1.0 — Initial reference specification

- Added universal bootstrap.
- Added core protocol.
- Added capability discovery and adaptation rules.
- Added execution, recovery, anti-loop, and handoff rules.
- Added safety and authority model.
- Added quality and evidence requirements.
- Added project memory and agent coordination rules.
- Added self-maintenance and self-improvement rules.
- Added machine-readable manifest, state, task, evidence, and capability schemas.
- Added reference project state, planning, knowledge, evidence, examples, and adapter guidance.
