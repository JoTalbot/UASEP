# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: M31-M40
- Owner: current maintenance session
- Scope: workflow policy, evidence freshness, stale-reference, ownership, handoff, and maintenance-runbook audits

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Completed hardening H01-H10, H11-H19, and H20 from repository evidence.
- Completed maintenance M11-M20 with focused protocol-invariant conformance assertions.
- Completed M21-M23: durable-state consistency, project-state synchronization, maintenance-plan rescore, and CI verification. Canonical CI runs #94 and #95 succeeded.
- Completed M24-M30: canonical bootstrap presence, manifest/state consistency, runtime-free active-tree constraints, skill inventory, examples references, and related conformance guards. CI run #101 succeeded on the verified M24-M30 commit.
- M31: read-only, main-scoped conformance workflow policy guard added.
- Latest M31-M40 verification: PENDING; current fixes must pass canonical CI.
- Unverified: Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.
- Blocked: NONE known.

## Evidence

- Fresh-agent acceptance: VERIFIED; `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`.
- Canonical conformance: VERIFIED / SUCCESS — runs #94 and #95 for M21-M23, and #101 for M24-M30.
- M21-M23 verification gate: VERIFIED by canonical runs #94 and #95.
- M24-M30 verification gate: VERIFIED by canonical run #101.
- M31-M40 current changes: present on `main`; latest verification pending.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- Historical references to retired runtime/AIOS2 architecture are provenance and are not treated as active-tree requirements.

## Next action

Verify the current M31-M40 CI run, fix any concrete regression, then continue the remaining M32-M40 audit work.

## Updated

- 2026-08-28 UTC
