# C5.1 Multi-agent Coordination

## Goal
Define coordination rules for multiple autonomous agents working inside UASEP.

## Capabilities

- Agent discovery
- Role assignment
- Task delegation
- Shared execution context
- Coordination state tracking
- Conflict escalation

## Coordination Flow

Request
↓
Agent Selection
↓
Task Distribution
↓
Execution
↓
Evidence Collection
↓
Consensus Review

## Safety Rules

- No agent bypasses verification requirements.
- Conflicting outputs require resolution.
- Unknown state must remain UNKNOWN until verified.
- All decisions require traceability.

## Status Model

READY
ACTIVE
WAITING
CONFLICT
BLOCKED
VERIFIED
