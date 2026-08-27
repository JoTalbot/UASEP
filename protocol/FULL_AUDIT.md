# UASEP Full Repository Audit

Audit baseline: current `main` commit `5f3810c51b014caa527a2f9bad750b83513f0812`.

## Verified architectural surfaces

- Canonical runtime orchestration exists in `runtime/runner.py` and `runtime/supervisor.py`.
- Acceptance verification is represented by `AcceptanceProvider` and `VerificationEngine`.
- Evidence and checkpoint persistence are explicit runtime dependencies.
- Project discovery validates the project root and reports UASEP state.
- Capability metadata records discovery, availability, approval requirement, and source.
- The autonomous development and runtime discovery contracts are documented under `protocol/`.
- Integration/conformance tests exist for capability discovery and autonomous development behavior.

## Release blockers

1. CI status for the current `main` head is not yet reported by the GitHub status API. A green release gate therefore cannot be claimed from repository metadata alone.
2. Repository-wide execution must be performed in a real checkout to validate imports, dependency installation, and all test paths together. Source inspection alone is insufficient evidence of a green suite.
3. The universal short prompt must not claim capabilities that the selected host has not explicitly exposed.
4. The final bootstrap must distinguish new-project initialization from resume and preserve authoritative `.uasep` state.

## Required final gates

- Run the complete test suite in a clean environment.
- Run conformance and integration suites separately and record results as evidence.
- Validate bootstrap/resume/crash recovery end-to-end.
- Validate the AIOS2 adapter contract end-to-end.
- Validate self-maintenance against UASEP itself.
- Only after these gates pass, publish the final universal short prompt.

## Audit rule

No feature is considered production-complete because its source file exists. Completion requires executable evidence, durable state where applicable, and a passing conformance gate.
