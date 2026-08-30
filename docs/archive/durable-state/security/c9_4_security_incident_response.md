# C9.4 Security Incident Response

## Purpose
Define controlled response workflows for detected security incidents.

## Capabilities

- incident classification
- response planning
- containment workflow
- recovery coordination
- evidence preservation
- post-incident learning

## Pipeline

Security Incident
↓
Classification
↓
Containment Decision
↓
Response Execution
↓
Verification
↓
Audit Update
↓
Knowledge Update

## States

- DETECTED
- ANALYZING
- CONTAINING
- RECOVERING
- RESOLVED
- ESCALATED
- UNKNOWN

## Rules

- every action requires traceability
- evidence must be preserved
- recovery must be verified
- unresolved incidents require escalation
