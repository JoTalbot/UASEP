# C90.3 Ecosystem Capability Discovery

## Purpose
Maintain a controlled inventory of capabilities exposed by connected systems.

## Capability record
Each capability records identity, provider, version, required permissions, supported inputs, outputs, limits, health, and policy constraints.

## Discovery rules
- Discovery is read-only by default.
- Untrusted metadata cannot expand permissions.
- New capabilities require validation before use.
- Deprecated or unhealthy capabilities are excluded from planning.
- Capability changes are auditable.

## Selection
Planning may select only capabilities whose permissions, health, compatibility, and policy status satisfy the current execution context.