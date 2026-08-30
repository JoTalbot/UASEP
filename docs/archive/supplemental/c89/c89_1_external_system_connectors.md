# C89.1 External System Connectors

## Purpose
Define a provider-neutral connector contract for safely integrating external systems.

## Design
- Explicit connector identity and capability declarations.
- Request/response envelopes with correlation IDs.
- Timeouts, retries, idempotency keys, and bounded concurrency.
- Least-privilege credentials supplied outside source control.
- Fail-closed behavior for unknown capabilities.
- Structured audit events for every external operation.

## Lifecycle
`discover -> validate -> authorize -> execute -> observe -> close`

## Safety invariants
1. No connector may bypass governance policies.
2. Credentials are never persisted in connector payloads.
3. External failures cannot corrupt internal state.
4. Retries must be bounded and idempotent where possible.
5. Connector health is independently observable.

## Validation
Contract tests should cover capability negotiation, authorization rejection, timeout handling, retry limits, malformed responses, and audit emission.
