# Agent Coordination Protocol

UASEP agents are interchangeable workers operating through chat and connected repository tools. Coordination is repository-native; no UASEP supervisor or runtime is required.

## Roles

Typical roles include researcher, architect, developer, tester, security reviewer, DevOps, documentation, and reviewer. Roles are capabilities, not permanent identities.

## Coordination

Every substantive task must define objective, scope/files, dependencies, write set, owner, acceptance criteria, risks, verification, and next action. Agents must not silently overwrite another active task's work.

## Parallel work

Analyze many tasks in parallel when useful. Execute together only tasks whose dependencies and write sets are compatible. Conflicting or dependent tasks wait for explicit coordination.

## Repository state

The repository is the durable shared memory. Before acting, restore `.uasep/state/` and inspect recent history. Before stopping, persist state and a handoff that is sufficient for an agent with no previous chat context.

## Evidence

Separate implementation from verification. Report `VERIFIED`, `PARTIALLY_VERIFIED`, `UNKNOWN`, or `FAILED`. Never fabricate tool results, tests, CI, commits, or external actions.

## Ownership

The agent assigned to a file owns its changes for the duration of the task. If two tasks need the same file, merge the work deliberately rather than letting one overwrite the other.

## Recovery

Record failures and lessons in `.uasep/knowledge/FAILURES.md`. Change strategy when a repeated approach fails. Preserve unrelated progress and use recoverable checkpoints or branches for risky operations.
