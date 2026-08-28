# UASEP Maintenance Runbook

## Purpose

Use this runbook for periodic repository-native maintenance of UASEP after a maintenance batch is verified.

## Before changing anything

1. Read `AGENTS.md` and restore durable context from `.uasep/state/`.
2. Confirm the working branch is `main` and inspect the current tree, recent commits, and applicable write set.
3. Read `protocol/CONFORMANCE.md` and `skills/SELF_MAINTENANCE.md` before consequential edits.
4. Check `state.json`, `STATUS.md`, `PROJECT_STATE.md`, `HANDOFF.md`, the active planning file, and recent evidence for drift.

## Audit sequence

Run repository-native checks for:

- protocol and manifest version consistency;
- machine-readable state and durable narrative consistency;
- evidence records and ownership records against their schemas;
- bootstrap, skills, examples, and referenced paths;
- runtime-free active-tree constraints;
- GitHub Actions workflow scope and read-only permissions;
- stale references to retired runtime architecture that could be mistaken for active requirements.

## Change rules

Prefer the smallest documentation-first change that fixes a confirmed defect or drift finding. Keep independent write sets separate, avoid parallel edits to the same file, and preserve historical evidence.

## Verification

After every consequential maintenance change:

1. Inspect the resulting diff.
2. Run `python -m pytest tests/conformance -q` locally when available.
3. Confirm the canonical GitHub Actions run for the resulting `main` commit is successful.
4. Record observed evidence using the repository evidence contract.
5. Synchronize `state.json`, `STATUS.md`, `PROJECT_STATE.md`, `HANDOFF.md`, and planning evidence when the task state changes.

## Failure handling

When verification fails, record the observed failure in `.uasep/knowledge/FAILURES.md`, identify the root cause before changing strategy, make the smallest corrective change, and re-run verification. Do not represent an unobserved or failed check as verified.

## Completion

A maintenance batch is complete only when its acceptance criteria are satisfied, evidence is recorded, and the canonical main-branch verification is green. When no concrete defect, drift finding, or new acceptance requirement exists, keep the repository in maintenance-complete state and do not invent additional work.

## Runtime boundary

UASEP remains runtime-free. Do not introduce a daemon, scheduler, database, supervisor, CLI, executable package, or runtime dependency unless a concrete user requirement demonstrates that the chat + GitHub-connected operating model cannot provide the required behavior.
