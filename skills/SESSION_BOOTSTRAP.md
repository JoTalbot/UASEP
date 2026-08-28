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
7. Check active ownership/write sets before editing.
8. Determine which GitHub-connected capabilities are actually available in this session.
9. Record any missing capability or ambiguous state as `UNKNOWN`/`BLOCKED`.
10. State the exact next action before consequential edits.

## Required output

Before editing, the agent should be able to identify:

- objective;
- current task and owner;
- branch;
- relevant files;
- dependencies;
- acceptance criteria;
- risks;
- verification plan;
- blockers or unknowns;
- next action.

## Prohibited behavior

Do not infer project state solely from chat memory. Do not claim a file was read, a test was run, a commit was created, or a GitHub side effect occurred unless the connected tools provide evidence.

## Completion

After work, update durable state and handoff so another agent can resume from the repository alone.
