# Project State

Status: ADOPTED

Protocol version: 3.4.0

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
- `protocol/CONFORMANCE.md` is version 3.4.0.
- Task, batch, evidence, readiness, and ownership contracts are defined and represented in `schemas/`.
- Universal bootstrap is aligned with the v3.4 workflow.
- Fresh-agent acceptance evidence is recorded in `.uasep/evidence/EV-UASEP-ACCEPT-2026-08-28.json`.
- Canonical conformance main-branch run #72 completed successfully at commit `0716c55d345a6843f09bb4c2fdc28d2113f60aeb`.
- M11-M20 protocol-invariant conformance coverage is recorded and verified.
- M21-M23 maintenance changes are present on `main`; the latest CI verification is pending.

## Unknown
- The latest maintenance commits have not yet completed a successful conformance run.
- Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.

## Next best actions
1. Verify the current main-branch conformance run and record its result.
2. Close M21-M23 only after the verification gate is satisfied.
3. Continue M24-M40 with evidence, bootstrap, skill, schema, state, runtime-free, CI, ownership, handoff, and maintenance-runbook audits.
4. Keep durable state, evidence, and handoff synchronized after consequential maintenance.

## Permanent constraint
Do not reintroduce executable runtime work unless a concrete user requirement demonstrates that chat + GitHub-connected agents cannot provide the needed behavior.
