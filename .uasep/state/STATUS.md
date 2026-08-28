# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: UASEP-HARDEN-2026-08-28
- Owner: current chat agent
- Scope: conformance fixtures, batch execution hardening, durable state synchronization

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Completed in current hardening batch: machine-readable state synchronization; 8 schema fixtures; fixture validation suite; runtime-free invariant checks; repository-native bootstrap/branch checks; explicit batch execution guide; CI evidence-boundary failure record; next-20-task plan.
- Remaining implementation work: NONE in the current documentation-first scope.
- Unverified: fresh independent-agent execution of the acceptance test; canonical automated CI execution.
- Blocked: NONE known.

## Evidence

- Repository changes: confirmed through successful GitHub content operations.
- Machine-readable state is validated by the state schema and aligned with manifest-level protocol/version/state/runtime values.
- Automated CI: UNKNOWN — no canonical workflow result has been observed through the available Actions interface.
- Fresh-agent acceptance: NOT_RUN.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- Historical references to retired runtime/AIOS2 architecture are provenance and are not treated as active-tree requirements.

## Next action

Run `examples/FRESH_AGENT_ACCEPTANCE.md` from a genuinely fresh agent/session with no originating chat history and record the result using `protocol/EVIDENCE_SCHEMA.md`. Separately, observe a canonical GitHub Actions run when available. If either produces defects, create targeted follow-up tasks rather than reopening completed hardening work.

## Updated

- 2026-08-28 UTC
