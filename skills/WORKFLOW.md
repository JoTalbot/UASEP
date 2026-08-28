# Skill: Canonical UASEP Workflow

Use this workflow for every substantive engineering task.

## 1. Discover

Inspect the repository, branch, recent commits, relevant files, available tools, and existing work ownership. Never assume the current state from chat alone.

## 2. Restore

Read `.uasep/state/HANDOFF.md`, `.uasep/state/PROJECT_STATE.md`, decisions, failures, and the relevant plan/backlog entries.

## 3. Audit

Identify the real root cause or objective. List affected files, dependencies, risks, acceptance criteria, and verification steps before editing.

## 4. Plan

Split work into independently executable tasks. Give each task an owner, write set, dependencies, acceptance criteria, and verification plan. Mark conflicting tasks explicitly.

## 5. Execute

Implement the smallest safe change. Prefer batches of independent tasks. Do not touch files owned by another active task without coordination.

## 6. Verify

Inspect the resulting diff and run the strongest available checks. Distinguish VERIFIED, INFERRED, UNKNOWN, and BLOCKED. Never invent unavailable CI or test results.

## 7. Integrate

Resolve conflicts deliberately. Preserve unrelated work. Ensure the combined result still satisfies every acceptance criterion.

## 8. Persist

Update plans, state, decisions, failures, and evidence. Record commit IDs and verification status.

## 9. Handoff

Leave the next agent an exact continuation point: current objective, completed work, unverified work, blockers, files/commits, and next action.
