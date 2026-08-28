# UASEP Master Plan

## Current phase — Adopted
- [x] Core protocol and agent contract
- [x] Capability discovery and readiness
- [x] Task, batch, ownership, verification, recovery, and handoff protocols
- [x] Durable state, evidence, decisions, and planning artifacts
- [x] Machine-readable schemas
- [x] Chat + GitHub Connector workflow
- [x] Conformance specification and practical acceptance scenarios
- [x] Adoption and multi-machine guidance
- [x] Runtime-free architecture
- [x] Machine-readable schema fixtures and repository-native conformance checks
- [x] Batch execution hardening and durable-state synchronization
- [x] Fresh-agent acceptance evidence recorded and reconciled as H20 complete

## Remaining validation
- [x] Run the complete fresh-agent acceptance pass from an independent session — evidence recorded in `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`
- [x] Record acceptance evidence in `.uasep/evidence/`
- [x] Resolve any defects discovered by that pass
- [x] Observe a canonical automated CI workflow run — main-branch run #44 verified successful

## Continuous maintenance
- [ ] Re-audit protocol/schema consistency after normative changes
- [ ] Update skills and examples when recurring failure patterns are discovered
- [ ] Maintain durable failure and decision knowledge
- [ ] Re-score `.uasep/planning/NEXT_20.md` when new requirements arrive

## Explicit non-goals

- No UASEP runtime is required.
- No local daemon or CLI is required.
- No AIOS2 integration is planned in the reference protocol.
- Code is added only when a concrete integration or validation need cannot be solved reliably with repository-native instructions and artifacts.
