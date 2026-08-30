# Project State

Status: ADOPTED

Protocol version: 3.5.0

## Objective
Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Architecture
Runtime-free. No UASEP daemon, CLI, scheduler, database, supervisor, or executable package is required.

## Current phase
Protocol v3.5.0 in progress (M63): folding the seven findings from the first real-world adoption (AIOS2) into the protocol. Previous: documentation-first hardening complete; M62 repaired the canonical CI and minimized the workflow set.

## Verified
- Protocol version is consistently 3.5.0 across VERSION, manifest, state.json, and CONFORMANCE.md (M63).
- `main` uses the pre-AIOS2 baseline.
- Retired runtime implementation, packaging, runtime tests, and runtime CI are not active requirements.
- `AGENTS.md` is the mandatory repository-wide agent contract.
- `skills/` contains reusable operational workflows.
- `protocol/CONFORMANCE.md` is version 3.5.
- Task, batch, evidence, readiness, and ownership contracts are defined and represented in `schemas/`.
- Universal bootstrap is aligned with the v3.4 workflow.
- Fresh-agent acceptance evidence is recorded in `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`.
- Canonical conformance main-branch run #72 completed successfully at commit `0716c55d345a6843f09bb4c2fdc28d2113f60aeb`.
- M11-M20 protocol-invariant conformance coverage is recorded and verified.
- M21-M23 maintenance verification gate is satisfied by canonical CI runs #94 and #95.
- M24-M30 maintenance verification gate is satisfied by canonical CI run #101 at commit `8f2998ecabe2a56ad3f2691d6a0cccbcf9d8e2ca`.
- M31-M40 maintenance verification gate is satisfied by canonical CI run #108 at commit `ec3cef1e8ec1aac01dd07c66218eeee88a9d50ec`.
- M41 added conformance guards that bind `VERSION` to durable protocol version and protect the canonical workflow's read-only, main-bounded checkout policy; run #120 succeeded at commit `bfb852e6d734b81256f930603c30cac68708c4a5`.
- M42 audited supplemental C81-C90 documentation; no executable runtime drift was found. Documentation-scope ambiguity is recorded as a maintenance finding.
- M62 (2026-08-30) repaired the canonical conformance workflow (checkout and setup-python had been removed by commit `0926002`, leaving the CI unable to run tests), replaced brittle string invariants with behavioral YAML-parsed checks, reduced the workflow set from 91 to 4 real workflows with policy enforced by `tests/conformance/test_workflow_policy.py`, removed nine orphaned root automation-engine state files, archived 456 non-normative documents to `docs/archive/`, rewrote the README to match reality, and added LICENSE and CODEOWNERS. Local conformance suite: 54 passed; canonical UASEP Main Conformance run 33298430803 succeeded on commit 52a8911.

## Unknown
- Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.
- (resolved) Canonical CI acceptance of the M62 batch was observed: run 33298430803 succeeded on commit 52a8911; see `.uasep/evidence/EV-UASEP-MAINT-M62-2026-08-30.json`.

## Next best actions
1. Perform repository-native periodic conformance/drift audits.
2. Open a new maintenance batch only when a concrete defect, drift finding, or new acceptance requirement exists.
3. Keep durable state, evidence, and handoff synchronized after consequential maintenance.

## Permanent constraint
Do not reintroduce executable runtime work unless a concrete user requirement demonstrates that chat + GitHub-connected agents cannot provide the needed behavior.

## Supplemental documentation
C81-C90 and the other non-normative cycle documents are archived under `docs/archive/`. They are not adopted roadmap stages and must not be interpreted as permission to add executable infrastructure without an explicit requirement.
