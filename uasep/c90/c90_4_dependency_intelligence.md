# C90.4 Dependency Intelligence

## Purpose
Model dependencies between connected capabilities and identify operational risk before execution.

## Dependency model
Each dependency records source, target, type, version constraints, health, criticality, fallback availability, and policy requirements.

## Analysis
- detect unavailable or degraded dependencies
- identify dependency chains and critical paths
- detect incompatible versions and contract drift
- estimate bounded blast radius
- prefer plans with safe fallbacks

## Guardrails
Dependency analysis is advisory unless an authorized policy explicitly permits an automated response. It cannot expand permissions or bypass governance.