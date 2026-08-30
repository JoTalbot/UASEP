# UASEP Release Connector

Release integration layer for controlled versioning and release orchestration.

## Responsibilities

- validate release prerequisites
- consume verified CI results
- prepare release metadata
- coordinate tag/release operations through an approved GitHub integration
- record release evidence

## Safety

Release actions must pass policy and verification gates before execution. Credentials are never stored in repository files.
