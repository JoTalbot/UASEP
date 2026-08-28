# Failed Approaches

## 2026-08-28 — Automated CI run not observed

Symptom: the conformance workflow was initially present on `main`, but the available GitHub Actions interface returned no workflow run or commit status for the CI commits checked.

Evidence: workflow file was present in `.github/workflows/conformance.yml`; the initial commit-level workflow lookup returned no run and combined status returned no checks.

Interpretation: CI status was `UNKNOWN` at that point. This was not evidence that the workflow or tests failed, and it was not evidence that they passed.

Resolution: stop changing the workflow blindly. Preserve the runtime-free CI definition and continue with repository-native conformance fixtures/tests. A later canonical run became observable.

## 2026-08-28 — Canonical CI cache prerequisite failure

Symptom: `actions/setup-python@v5` failed because `cache: pip` requires `requirements.txt` or `pyproject.toml`, neither of which exists in the runtime-free repository.

Evidence: canonical workflow job logs identified the missing dependency manifest prerequisite.

Resolution: minimally removed `cache: pip` while preserving Python 3.12, explicit validation dependencies, and the conformance pytest command. The repaired canonical workflow subsequently completed successfully in run #44.

## Maintenance rule

Record recurring failures here with symptom, evidence, attempted strategy, root cause if known, and successful resolution. Do not convert unavailable evidence into a success claim.
