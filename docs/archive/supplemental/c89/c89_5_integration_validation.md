# C89.5 Integration Validation

## Validation gates
- connector configuration validation
- authentication and authorization checks
- request and response schema validation
- timeout and retry policy validation
- idempotency checks for side effects
- audit-event verification
- failure and fallback-path verification

## Acceptance criteria
An integration is valid only when its inputs, outputs, permissions, failure behavior, and observability are explicitly defined and testable.

## Failure handling
External failures must remain isolated from core runtime state. Errors are classified, recorded, and routed through bounded recovery paths.