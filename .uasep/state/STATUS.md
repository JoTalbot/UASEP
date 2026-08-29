# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: NONE
- Owner: NONE
- Scope: periodic conformance/drift audits only

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Completed hardening H01-H10, H11-H19, and H20 from repository evidence.
- Completed maintenance M11-M20 with focused protocol-invariant conformance assertions.
- Completed M21-M23: durable-state consistency, project-state synchronization, maintenance-plan rescore, and CI verification.
- Completed M24-M30: bootstrap, manifest/state, runtime-free, skill, example, schema/fixture, version, and active-tree conformance guards.
- Completed M31-M40: workflow-policy, evidence freshness, stale-reference, ownership, handoff, status, acceptance linkage, decision/failure, and maintenance-runbook audits.
- Completed M41: VERSION-to-state consistency and canonical CI read-only/main-bounded policy guards.
- Completed M42: audited C81-C90 supplemental documentation against canonical runtime-free scope; no executable architecture drift found.
- Completed M60: Canonical CI acceptance pass. Main Conformance run 33275234855 succeeded after evidence schema corrections.
- Completed M61: durable-state reconciliation after successful canonical validation.
- Current maintenance batches: COMPLETE. No active task.

## Evidence

- Fresh-agent acceptance: VERIFIED.
- Canonical conformance: VERIFIED / SUCCESS.
- M60 verification: VERIFIED by successful GitHub Actions run 33275234855.
- M61 reconciliation: VERIFIED by durable state update after CI acceptance.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- C81-C90 are supplemental architecture documentation, not adopted normative roadmap stages, unless a concrete future requirement explicitly promotes them.

## Next action

Perform repository-native periodic conformance/drift audits. Open a new maintenance batch only when a concrete defect, drift finding, or new acceptance requirement exists.

## Updated

- 2026-08-29 UTC
