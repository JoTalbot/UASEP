ID: UASEP-MAINT-M41-2026-08-29
OBJECTIVE: Add repository-native guards for version consistency and the read-only main-branch CI policy.
OWNER: ChatGPT / GitHub-connected agent
BRANCH: main
WRITE_SET: tests/conformance/test_protocol_invariants.py; .uasep/state/TASK_UASEP-MAINT-M41-2026-08-29.md; .uasep/state/BATCH_UASEP-MAINT-M41-2026-08-29.md; .uasep/state/state.json; .uasep/state/STATUS.md; .uasep/state/HANDOFF.md; .uasep/planning/NEXT_20.md
DEPENDENCIES: NONE
CONFLICTS: NONE
ACCEPTANCE:
- Conformance tests assert VERSION matches durable protocol version.
- Conformance tests assert the canonical workflow has contents read permission, checks out main, and uses shallow checkout.
- Changes are committed to main and canonical CI is observed.
- Durable state records the result and evidence.
RISK: LOW
VERIFICATION:
- Review changed test logic against current VERSION and workflow.
- Run tests through canonical GitHub Actions workflow triggered by the main commit.
- Record resulting CI evidence.
STATUS: IN_PROGRESS
