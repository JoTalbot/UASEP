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

## Remaining validation
- [ ] Run the complete fresh-agent acceptance pass from an independent session
- [ ] Record acceptance evidence in `.uasep/evidence/`
- [ ] Resolve any defects discovered by that pass

## Continuous maintenance
- [ ] Re-audit protocol/schema consistency after normative changes
- [ ] Update skills and examples when recurring failure patterns are discovered
- [ ] Maintain durable failure and decision knowledge

## Explicit non-goals

- No UASEP runtime is required.
- No local daemon or CLI is required.
- No AIOS2 integration is planned in the reference protocol.
- Code is added only when a concrete integration or validation need cannot be solved reliably with repository-native instructions and artifacts.
