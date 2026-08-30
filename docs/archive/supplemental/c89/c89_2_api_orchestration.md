# C89.2 API Orchestration

## Purpose
Provide a controlled orchestration layer for calls across internal and external APIs.

## Responsibilities
- Route requests to declared capabilities.
- Propagate correlation and trace identifiers.
- Enforce authentication, authorization, rate limits, and deadlines.
- Normalize provider-specific errors into stable internal outcomes.
- Support circuit breaking and bounded retries.
- Emit auditable execution records.

## Execution model
`intent -> policy check -> route -> execute -> normalize -> record`

## Invariants
- Policy evaluation occurs before external side effects.
- No untrusted response becomes executable instruction without validation.
- Timeouts and retry budgets are mandatory.
- Partial failures are explicit and recoverable.

## Validation
Test routing, authorization failures, rate limiting, timeout propagation, circuit breaking, malformed provider responses, and trace continuity.
