# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: M24-M30
- Owner: current maintenance session
- Scope: evidence, bootstrap, skill, example, schema/state, and runtime-free conformance guards

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Completed hardening H01-H10, H11-H19, and H20 from repository evidence.
- Completed maintenance M11-M20 with focused protocol-invariant conformance assertions.
- Completed M21-M23: durable-state consistency, project-state synchronization, maintenance-plan rescore, and CI verification. Canonical CI runs #94 and #95 succeeded.
- Added M24-M30 conformance guards for canonical bootstrap presence, manifest/state consistency, runtime-free active-tree constraints, skill inventory, and examples referencing normative protocol material.
- Latest M24-M30 verification: PENDING; new canonical CI will validate the current main state.
- Unverified: Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.
- Blocked: NONE known.

## Evidence

- Fresh-agent acceptance: VERIFIED; `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`.
- Canonical conformance: VERIFIED / SUCCESS — runs #94 and #95.
- M21-M23 verification gate: VERIFIED by canonical runs #94 and #95.
- M24-M30 repository changes: present on `main`; CI verification pending.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- Historical references to retired runtime/AIOS2 architecture are provenance and are not treated as active-tree requirements.

## Next action

Verify M24-M30 with the canonical GitHub Actions run, then continue M31-M40.

## Updated

- 2026-08-28 UTC
