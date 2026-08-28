# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: M21-M23
- Owner: current maintenance session
- Scope: durable-state consistency, project-state synchronization, and maintenance-plan rescore

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Completed hardening H01-H10, H11-H19, and H20 from repository evidence.
- Completed maintenance M11-M20: focused automated conformance assertions for bootstrap, readiness, task/batch contracts, capability honesty, evidence, recovery, failure/ownership handling, and destructive-operation safeguards.
- Corrected durable-state drift in `.uasep/state/PROJECT_STATE.md`.
- Added a durable-state narrative consistency assertion to `tests/conformance/test_protocol_invariants.py`.
- Re-scored `.uasep/planning/NEXT_20.md` into maintenance batch M21-M40.
- Canonical conformance: VERIFIED / SUCCESS — main-branch run #72 at its tested commit `0716c55d345a6843f09bb4c2fdc28d2113f60aeb`.
- Latest maintenance changes: verification PENDING; no new CI result is currently visible through the available connector actions.
- Unverified: Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.
- Blocked: NONE known.

## Evidence

- Fresh-agent acceptance: VERIFIED; `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`.
- Canonical conformance: VERIFIED / SUCCESS — main-branch run #72.
- H11-H19 verification: `EV-UASEP-BATCH-H11-H19-2026-08-28.json`.
- M11-M20 verification: `EV-UASEP-MAINT-M11-20-2026-08-28.json`.
- M21-M23 repository writes: confirmed by successful GitHub content operations; test execution remains pending.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- Historical references to retired runtime/AIOS2 architecture are provenance and are not treated as active-tree requirements.

## Next action

Verify the M21-M23 maintenance changes, then continue M24-M40 from `.uasep/planning/NEXT_20.md`.

## Updated

- 2026-08-28 UTC
