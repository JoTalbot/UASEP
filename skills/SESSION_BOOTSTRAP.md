# Skill: Session Bootstrap

Use this skill at the start of every new chat session or after a context interruption.

## Goal

Reconstruct enough durable context to work safely without relying on previous chat history.

## Procedure

1. Read `AGENTS.md`.
2. Identify the repository and exact assigned branch.
3. Read `.uasep/state/STATUS.md`.
4. Read `.uasep/state/PROJECT_STATE.md` and `.uasep/state/HANDOFF.md` when present.
5. Read the relevant plan/backlog and applicable protocol/skill.
6. Inspect recent repository history and the files named by the current task.
7. Establish Agent Readiness using `protocol/AGENT_READINESS.md`.
8. Create or restore the applicable Task Contract using `protocol/TASK_CONTRACT.md`.
9. If multiple tasks are being handled together, create/restore a Batch Manifest using `protocol/BATCH_MANIFEST.md`.
10. Check active ownership/write sets before editing.
11. Determine which GitHub-connected capabilities are actually available in this session.
12. Record any missing capability or ambiguous state as `UNKNOWN`/`BLOCKED`.
13. State the exact next action before consequential edits.

## Required output

Before editing, the agent should be able to identify:

- objective;
- current task and owner;
- branch;
- relevant files;
- dependencies and conflicts;
- acceptance criteria;
- risk;
- verification plan;
- blockers or unknowns;
- next action.

## Prohibited behavior

Do not infer project state solely from chat memory. Do not claim a file was read, a test was run, a commit was created, or a GitHub side effect occurred unless the connected tools provide evidence.

## Completion

After work, update durable state, evidence, and handoff so another agent can resume from the repository alone.
