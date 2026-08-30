# Handoff

Current objective: maintain UASEP as a complete repository-native operating protocol for AI agents working through chat and GitHub Connector.

Current step: M62 maintenance batch (CI repair, workflow minimization, documentation archive, repository hygiene) is complete and pushed to `main`. Local conformance suite: 54 passed. The canonical UASEP Main Conformance run for the pushed batch is pending observation; when observed, update `EV-UASEP-MAINT-M62-2026-08-30.json`, `STATUS.md`, `state.json`, and this handoff with the run result and final commit SHA.

Completed in M62:
- diagnosed that commit `0926002` ("remove deprecated node20 action dependencies") had removed checkout and setup-python from `.github/workflows/conformance.yml`, leaving the canonical CI unable to execute the pytest suite, and that the invariant test `test_canonical_workflow_is_read_only_and_main_bounded` failed (1 failed, 43 passed);
- restored the canonical workflow with full-SHA-pinned checkout (ref: main, fetch-depth: 1) and setup-python, replaced the every-5-minute cron with a daily drift check, and removed the debug diagnostics step;
- rewrote the brittle workflow invariant as a behavioral YAML-parsed check and added `tests/conformance/test_workflow_policy.py` (inventory lock, explicit permissions, write allowlist, full-SHA pinning, checkout presence, at-most-daily cron, real test execution, deliberate release flow, secret scan) — 10 tests;
- deleted 87 non-functional workflows, retaining `conformance.yml`, `release-gate.yml`, `automated-release.yml`, `release-verification.yml`; made the release gate manual-dispatch-only and added dependency installation so its pytest step can run;
- removed nine orphaned automation-engine state files from the repository root (including dead references to JoTalbot/AIOS and JoTalbot/AIOS2);
- archived 456 non-normative documents to `docs/archive/` (`.uasep/` now holds only manifest.yaml plus state/, planning/, knowledge/, evidence/, decisions/);
- rewrote `README.md` to match the actual structure; added `LICENSE` (MIT) and `.github/CODEOWNERS`; added documentation-restraint rules to `protocol/SELF_MAINTENANCE.md`;
- recorded the task contract, ownership lease, and evidence for M62 in durable state.

Current task: NONE.

Unverified:
- Canonical GitHub Actions conformance run for the pushed M62 batch had not been observed when this handoff was written.
- Historical search indexes may retain provenance from retired runtime/AIOS2 architecture.

Blockers: none known.

Next action:
1. Observe the canonical conformance run for the M62 batch and record the result in evidence and durable state.
2. Use the canonical conformance workflow for scheduled drift audits (it now runs daily).
3. Open individual maintenance tasks only when a concrete defect, drift finding, or new acceptance requirement is found.
4. Keep `state.json`, `STATUS.md`, `PROJECT_STATE.md`, `HANDOFF.md`, and planning evidence synchronized after consequential changes.

Evidence status: H01-H20, M11-M20, M21-M23, M24-M30, M31-M40, M41, and M42 are VERIFIED / COMPLETE. M43-M61 remain PARTIALLY_VERIFIED at the individual-item level. M62 is PARTIALLY_VERIFIED pending canonical CI observation; local conformance verification passed (54/54).

Note: `main` is the working branch. Do not create a feature branch for routine maintenance unless the repository contract changes.

Supplemental documentation note: C81-C90 and other non-normative cycle documents are archived in `docs/archive/`. They are not adopted roadmap stages and do not authorize executable infrastructure.
