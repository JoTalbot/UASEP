# UASEP End-to-End Orchestrator

## Purpose

Define the canonical orchestration flow connecting repository discovery, policy evaluation, scheduling, runtime execution, verification, evidence, and reporting.

## Flow

Repository Registry
→ Policy Engine
→ Job Scheduler
→ Runtime Manager
→ GitHub / CI / Release / Notification Connectors
→ Verification Engine
→ Evidence Sync
→ State Manager
→ Metrics / Reporting

## Gates

1. Policy approval before execution.
2. Permission validation before actions.
3. Verification before completion.
4. Evidence persistence for every material operation.
5. Failed verification routes to recovery analysis instead of silently completing.

## Idempotency

Operations should use stable operation identifiers and avoid repeating completed mutations.

## Secrets

Credentials and tokens must be supplied through the execution environment or GitHub secrets. They must never be committed to repository files or logs.
