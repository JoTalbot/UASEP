# Multi-Machine Handoff Example

UASEP supports agents working from different machines because the repository is the durable coordination surface.

## Agent A

Agent A claims a task with an explicit write set, performs the allowed changes, verifies what it can, and records:

- task and owner;
- branch;
- changed files/commit;
- verification status and evidence;
- unresolved risks or blockers;
- ownership release or transfer;
- exact next action.

## Agent B

Agent B starts without relying on Agent A's chat history. It reads `AGENTS.md`, `.uasep/state/STATUS.md`, `PROJECT_STATE.md`, and `HANDOFF.md`, then inspects the referenced commit/files and reconciles ownership before editing.

## Continuation rule

If Agent B cannot establish what was completed or which scope is safe to modify, it remains `BLOCKED`/`UNKNOWN` and records the missing evidence instead of guessing.

## Acceptance

The handoff is successful when Agent B can continue from repository state alone and no critical instruction or continuation fact exists only in the previous machine's chat.
