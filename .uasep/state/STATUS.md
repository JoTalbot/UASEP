# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: UASEP-MAINT-M63-2026-08-30
- Owner: arena-ai-coding-agent
- Scope: v3.5.0 adoption hardening (fold AIOS2 dogfooding findings into the protocol)

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Completed hardening H01-H10, H11-H19, and H20 from repository evidence.
- Completed maintenance M11-M20 with focused protocol-invariant conformance assertions.
- Completed M21-M23: durable-state consistency, project-state synchronization, maintenance-plan rescore, and CI verification.
- Completed M24-M30: bootstrap, manifest/state, runtime-free, skill, example, schema/fixture, version, and active-tree conformance guards.
- Completed M31-M40: workflow-policy, evidence freshness, stale-reference, ownership, handoff, status, acceptance linkage, decision/failure, and maintenance-runbook audits.
- Completed M41: VERSION-to-state consistency and canonical CI read-only/main-bounded policy guards.
- Completed M42: audited C81-C90 supplemental documentation against canonical runtime-free scope; no executable architecture drift found.
- Completed M60-M61: canonical CI acceptance pass (run 33275234855) and durable-state reconciliation.
- Completed M62 (2026-08-30): repaired the broken canonical conformance workflow, replaced echo-only workflows with real policy tests, minimized the workflow set to four, archived 456 non-normative documents to docs/archive/, reconciled README and root state files, added LICENSE and CODEOWNERS, and codified documentation restraint.
- Released v3.4.0 (2026-08-30) through the deliberate release flow; merged Dependabot PR #66 (actions/checkout v7.0.1).
- Completed M63 (2026-08-30): protocol v3.5.0 — uasep_runtime schema semantics, project_runtime/project extension, reference-vs-copy adoption guidance, LEGACY_MIGRATION skill, branch lifecycle rules, portable conformance kit.
- Current maintenance batches: M63 in progress (protocol v3.5.0); the reference project itself remains ADOPTED.

## Evidence

- Fresh-agent acceptance: VERIFIED.
- Canonical conformance: VERIFIED / SUCCESS.
- M60 verification: VERIFIED by successful GitHub Actions run 33275234855.
- M61 reconciliation: VERIFIED by durable state update after CI acceptance.
- M62 finding: VERIFIED — commit 0926002 had removed checkout/setup-python from the canonical conformance workflow, so the canonical CI could not execute the test suite (local run: 1 failed, 43 passed). The runs recorded earlier as "canonical acceptance" (#651, #295) exercised only trivial file-existence/echo workflows that M62 removed.
- M62 repair: VERIFIED — local conformance suite 54 passed, and canonical UASEP Main Conformance run 33298430803 succeeded on commit 52a8911 (job log: '54 passed'). Evidence: EV-UASEP-MAINT-M62-2026-08-30.json.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- M62: the GitHub Actions workflow set is deliberately minimal (conformance, release-gate, automated-release, release-verification). Workflow policy is enforced by tests/conformance/test_workflow_policy.py, not by decorative workflows. Releases are deliberate: the gate is manual dispatch and automated release only fires after a passing gate.
- M62: non-normative cycle documentation lives in docs/archive/ and never authorizes executable infrastructure.

- Release v3.4.0: VERIFIED — gate run 33299034737, automated-release run 33299048999, tag v3.4.0 -> df12ee3, published release confirmed. Evidence: EV-UASEP-RELEASE-V3.4.0-2026-08-30.json.

## Next action

Perform repository-native periodic conformance/drift audits. Open a new maintenance batch only when a concrete defect, drift finding, or new acceptance requirement exists.

## Updated

- 2026-08-30 UTC
