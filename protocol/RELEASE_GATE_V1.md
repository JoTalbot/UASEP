# UASEP v1.0 Release Gate

UASEP v1.0 is eligible for release when all mandatory gates below have durable evidence.

- [x] Universal bootstrap contract exists.
- [x] Runtime discovery contract exists.
- [x] Capability discovery distinguishes discovered, available, approval-required, and source metadata.
- [x] Canonical development contract requires verification before completion.
- [x] Checkpoint/resume behavior has integration coverage.
- [x] Self-development contract has conformance coverage.
- [x] Canonical validator is used by CI.
- [x] CI has completed successfully on the validated main revision across Python 3.10, 3.11, and 3.12.
- [x] Universal short prompt is versioned as v1.0.

## Release semantics

Passing this gate means the repository satisfies its automated validation contract. It does not grant a host capabilities that the host has not exposed, and it does not claim arbitrary software projects will complete without project-specific requirements, credentials, approvals, or external dependencies.

## Post-release evolution

Future changes MUST preserve the autonomous lifecycle: discover → bootstrap/resume → plan → execute → verify → evidence → checkpoint → recover/replan → continue. A change that weakens these guarantees requires a new explicit contract and validation evidence.
