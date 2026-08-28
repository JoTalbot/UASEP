# Project State

Status: ADOPTED

## Objective
Maintain UASEP as a complete runtime-free operating protocol for AI agents working through chat and GitHub-connected tools.

## Architecture
Runtime-free. No UASEP daemon, CLI, scheduler, database, supervisor, or executable package is required.

## Current phase
Adopted; documentation-first protocol hardening is complete for the current scope.

## Verified
- `main` uses the pre-AIOS2 baseline.
- Retired runtime implementation, packaging, runtime tests, and runtime CI are not active requirements.
- `AGENTS.md` is the mandatory repository-wide agent contract.
- `skills/` contains reusable operational workflows.
- `protocol/CONFORMANCE.md` is version 3.4.
- Task, batch, evidence, readiness, and ownership contracts are defined and represented in `schemas/`.
- Universal bootstrap is aligned with the v3.4 workflow.
- Fresh-agent acceptance evidence is recorded in `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`.
- Canonical conformance main-branch run #72 completed successfully at commit `0716c55d345a6843f09bb4c2fdc28d2113f60aeb`.
- M11-M20 protocol-invariant conformance coverage is recorded and verified.

## Unknown
- Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.
- The latest handoff-only commit `7d5a028f9b0704096978cc44a034282293f53b64` has no individual commit status attached; the referenced canonical conformance result remains the verified run #72 at its tested commit.

## Next best actions
1. Continue repository-native maintenance/conformance audits when requirements or normative artifacts change.
2. Re-score `.uasep/planning/NEXT_20.md` and open the next maintenance batch when a concrete drift or improvement target is identified.
3. Keep durable state, evidence, and handoff synchronized after consequential maintenance.

## Permanent constraint
Do not reintroduce executable runtime work unless a concrete user requirement demonstrates that chat + GitHub-connected agents cannot provide the needed behavior.
