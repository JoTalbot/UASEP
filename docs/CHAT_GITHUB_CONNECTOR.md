# Chat + GitHub Connector Operating Guide

UASEP assumes the host AI agent and its connected GitHub tools perform all execution. The repository stores the durable context.

## Start a task

Use a concise instruction describing the objective. The agent must then read `AGENTS.md`, restore `.uasep/state/`, inspect the repository, and identify the applicable skill.

## Resume work

Do not rely on previous chat history. Read the handoff, project state, plan, decisions, failures, and recent commits. Confirm the actual branch and files before editing.

## Work in batches

Analyze many candidate tasks together. For each task record files/write set, dependencies, owner, risks, acceptance criteria, and verification. Execute only independent tasks together.

## GitHub changes

Prefer atomic commits with descriptive messages. Never claim a push unless the GitHub operation succeeded. When multiple agents work concurrently, use separate branches or explicitly coordinated non-overlapping write sets.

## Verification

Inspect the final diff and use the strongest available repository checks. GitHub Actions are optional evidence when configured; absence of CI is `UNKNOWN`, not success.

## Handoff

Before stopping, update `.uasep/state/HANDOFF.md`. Another agent must be able to continue using repository files alone.

## Recovery

For failures, record the symptom, evidence, attempted strategy, root cause if known, and next strategy in `.uasep/knowledge/FAILURES.md`. Preserve unrelated progress.

## Important limitation

A chat-connected agent cannot honestly claim work that its available tools did not perform. UASEP compensates with explicit state, evidence, and handoff rather than pretending to provide autonomous execution infrastructure.
