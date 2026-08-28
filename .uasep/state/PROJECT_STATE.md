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

## Unknown
- Fresh-agent acceptance test has not yet been executed as a complete independent pass.
- Automated CI status is not established for the documentation-first protocol.
- Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.

## Next best actions
1. Run `examples/FRESH_AGENT_ACCEPTANCE.md` from a genuinely fresh agent/session.
2. Record the result using `protocol/EVIDENCE_SCHEMA.md`.
3. Perform additional conformance/drift audits when the protocol or project requirements change.

## Permanent constraint
Do not reintroduce executable runtime work unless a concrete user requirement demonstrates that chat + GitHub-connected agents cannot provide the needed behavior.
