# Changelog

## 3.2.0-new — Unification branch (`new`)

- Documented target design (`TARGET_DESIGN.md`).
- Introduced single Task model aligned with `schemas/task.schema.json`.
- Introduced `TaskGraph` with unknown-dep, self-dep, and cycle validation.
- Introduced unified `Store` (state.json, graph.json, evidence log, checkpoints).
- Introduced canonical `Supervisor.run_once` / `run_until_idle` with mandatory verification.
- Added `schemas/graph.schema.json`; tightened state/task schemas.
- Persisted reference `.uasep/graph.json` and updated handoff/state/manifest.
- Added conformance/integration tests for unified graph and supervisor.

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
