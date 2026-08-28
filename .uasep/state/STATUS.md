# UASEP Durable Status

## Objective

Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Phase

- Phase: ADOPTED

## Current task

- ID: UASEP-PROTO-001
- Owner: current chat agent
- Scope: protocol, documentation, durable state, examples

## Progress

- Completed: runtime-free architecture; legacy runtime state/tests removed; conformance specification aligned to v3.4; mandatory agent contract and workflow skills established; canonical task lifecycle, ownership/lease, task contract, batch manifest, evidence schema, and readiness protocol added; session bootstrap and practical conformance scenarios added; multi-machine, conflict/recovery, new-project, existing-project adoption, parallel-batch, drift-detection, and fresh-agent acceptance guidance added.
- Remaining implementation work: NONE in the current documentation-first scope.
- Unverified: fresh independent-agent execution of the acceptance test; historical search indexes may retain provenance from retired architecture.
- Blocked: NONE known.

## Evidence

- Repository changes: confirmed through successful GitHub content operations.
- Automated CI: UNKNOWN — no canonical automated CI result is established for the documentation-first protocol.
- Fresh-agent acceptance: NOT_RUN.

## Decisions

- UASEP remains runtime-free. Do not add executable infrastructure unless a concrete connector/chat limitation requires it.
- `.uasep/state/` is the canonical durable operational state.
- `protocol/` is normative; `AGENTS.md` is the mandatory project contract; `skills/` are reusable procedures; examples illustrate compliant behavior.
- Historical references to retired runtime/AIOS2 architecture are provenance and are not treated as active-tree requirements.

## Next action

Run `examples/FRESH_AGENT_ACCEPTANCE.md` from a genuinely fresh agent/session with no originating chat history. Record the result using `protocol/EVIDENCE_SCHEMA.md`. If it passes, UASEP's documentation-first adoption can be considered acceptance-tested for this scope.

## Updated

- 2026-08-28 UTC
