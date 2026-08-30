# C89.6 Integration Intelligence Tests

## Test matrix
- valid external event is accepted
- malformed payload is rejected
- unauthorized action is denied
- policy violation blocks side effects
- timeout produces bounded failure
- retry budget is enforced
- duplicate event remains idempotent where required
- audit record is produced for integration decisions
- connector failure does not corrupt core runtime state
- fallback path is deterministic

## Exit criteria
All integration safety gates have explicit automated test coverage before an integration is considered production-ready.