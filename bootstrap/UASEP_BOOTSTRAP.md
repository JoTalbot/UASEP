# UASEP Universal Bootstrap

Use UASEP as a repository-native operating protocol for AI agents working through chat and connected GitHub tools. UASEP has no runtime, daemon, CLI, or autonomous executor.

## Bootstrap

Before consequential work:

1. Discover the repository, exact assigned branch, applicable project instructions, available connected capabilities, and recent history.
2. Read `AGENTS.md` and the relevant skill.
3. Restore `.uasep/state/STATUS.md`, `PROJECT_STATE.md`, and `HANDOFF.md`.
4. Read the relevant backlog/plan and normative protocol sections.
5. Establish Agent Readiness using `protocol/AGENT_READINESS.md`.
6. Create or restore a Task Contract using `protocol/TASK_CONTRACT.md`.
7. For multi-task work, create or restore a Batch Manifest using `protocol/BATCH_MANIFEST.md`.
8. Inspect ownership/write sets before editing.

## Operating loop

**DISCOVER → RESTORE STATE → READINESS → TASK CONTRACT → ANALYZE → CLAIM → BATCH → EXECUTE → VERIFY → EVIDENCE → UPDATE STATE → HANDOFF**

Use only capabilities actually available in the current session. Missing or ambiguous capabilities are `UNKNOWN`/`BLOCKED`; never fabricate side effects.

## Parallel work

Analyze multiple tasks together when useful. Classify each task as `INDEPENDENT`, `DEPENDENT`, `CONFLICTING`, or `BLOCKED`. Execute together only when dependencies, ownership, and write sets are compatible. Conflicts are coordinated or serialized.

## Verification

Every consequential result requires evidence proportional to risk. Record evidence using `protocol/EVIDENCE_SCHEMA.md`. A successful repository operation proves only that operation succeeded; it does not prove tests, CI, review, deployment, or external effects.

Use `VERIFIED`, `PARTIALLY_VERIFIED`, `UNKNOWN`, or `FAILED` accurately. `DONE` requires satisfied acceptance criteria plus evidence.

## Recovery and handoff

After interruption, reconstruct state from repository artifacts and actual files/commits. Do not assume unfinished work completed. Before stopping, update durable status and handoff with completed/unverified work, blockers, ownership, changed files/commits, evidence, and the next safe action.

## Safety

Use checkpoints and explicit approval for destructive or irreversible actions. Never overwrite another active agent's work without deliberate coordination. Do not repeatedly retry an unchanged failed strategy.

## Goal

Keep the project understandable, verifiable, maintainable, and continuable by a fresh agent with no previous chat history.
