# Changelog

## Maintenance 2026-08-30 — CI repair and repository hygiene (M62)

- Repaired the canonical conformance workflow: restored the full-SHA-pinned checkout (`ref: main`, `fetch-depth: 1`) and setup-python steps that commit `0926002` had removed, dropped the debug diagnostics step, and replaced the every-5-minute cron with a daily drift check.
- Replaced the brittle string-matching CI invariant with a behavioral, YAML-parsed check.
- Added `tests/conformance/test_workflow_policy.py`: workflow inventory lock, explicit permissions, write-permission allowlist, full-SHA action pinning, checkout presence, at-most-daily cron, real test execution, deliberate release flow, and a repository secret scan.
- Reduced the workflow set from 91 to four real workflows (`conformance`, `release-gate`, `automated-release`, `release-verification`) and deleted 87 echo-only stubs and dead orchestration chains.
- Made the release chain deliberate: the release gate is manual dispatch and now installs its test dependencies; automated release only fires after a passing gate.
- Removed nine orphaned automation-engine state files from the repository root (including dead references to JoTalbot/AIOS and JoTalbot/AIOS2).
- Archived 456 non-normative C-cycle and retired-runtime documents to `docs/archive/`; `.uasep/` now contains only canonical durable state.
- Rewrote the README to match the actual repository structure; added an MIT LICENSE and CODEOWNERS.
- Added documentation-restraint rules to `protocol/SELF_MAINTENANCE.md`.

## 3.4.0 — Runtime-free protocol hardening

- Formalized Agent Readiness, Task Contract, Batch Manifest, Evidence, and Ownership protocols.
- Aligned universal bootstrap, agent contract, durable state, and conformance specification to v3.4.
- Added and hardened machine-readable schemas for task, batch, evidence, readiness, ownership, state, capabilities, and project manifest.
- Added fresh-agent acceptance guidance and strengthened parallel-work, recovery, evidence, ownership, and connector invariants.
- Confirmed the current scope remains runtime-free and designed for chat plus connected GitHub tools.

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
