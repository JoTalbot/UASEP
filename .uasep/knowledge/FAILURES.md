# Failed Approaches

## 2026-08-28 — Automated CI run not observed

Symptom: the conformance workflow is present on `main`, but the available GitHub Actions interface returned no workflow run or commit status for the CI commits checked.

Evidence: workflow file is present in `.github/workflows/conformance.yml`; commit-level workflow lookup returned no run and combined status returned no checks.

Interpretation: CI status remains `UNKNOWN`. This is not evidence that the workflow or tests failed, and it is not evidence that they passed.

Resolution: stop changing the workflow blindly. Preserve the runtime-free CI definition and continue with repository-native conformance fixtures/tests. Revisit CI execution when a canonical workflow run is observable.

## Maintenance rule

Record recurring failures here with symptom, evidence, attempted strategy, root cause if known, and successful resolution. Do not convert unavailable evidence into a success claim.
