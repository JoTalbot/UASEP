# Project State

Status: ACTIVE

## Objective
Maintain UASEP as a portable, verifiable operating protocol for AI agents using chat and GitHub-connected tools.

## Architecture
Runtime-free. No UASEP daemon, CLI, scheduler, database, supervisor, or executable package is required.

## Current phase
Protocol hardening and operationalization.

## Verified
- `main` is based on the pre-AIOS2 baseline.
- Runtime implementation, runtime packaging, runtime tests, and runtime CI have been retired from the active tree.
- Repository-wide agent contract exists at `AGENTS.md`.
- Reusable operational skills exist under `skills/`.
- README describes the connector-first model.

## Unknown
- Full documentation consistency audit is not yet complete.
- Connector-specific limits and best practices need explicit documentation.

## Next best actions
1. Normalize protocol and example documents for runtime-free operation.
2. Add ChatGPT + GitHub Connector operating guide.
3. Define durable task, batch, status, decision, failure, and evidence templates.
4. Strengthen multi-agent ownership and handoff rules.
5. Add practical examples for starting, resuming, parallelizing, verifying, and recovering work.

## Permanent constraint
Do not reintroduce executable runtime work unless a concrete user requirement demonstrates that chat + GitHub-connected agents cannot provide the needed behavior.
