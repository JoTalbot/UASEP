# UASEP Short Bootstrap Protocol

Use this protocol as the small, host-neutral instruction placed in ChatGPT, a local CLI agent, or a temporary agent environment.

## Bootstrap

1. Treat UASEP as the project's autonomous development control plane.
2. Discover the current project root and available host capabilities before modifying files.
3. Locate and load the project's UASEP protocol, state, decisions, constraints, and evidence. Prefer repository-local UASEP state over assumptions from the chat.
4. If UASEP is absent, bootstrap it using the repository's supported launcher without overwriting existing project artifacts.
5. Inspect the current implementation before planning. Do not restart completed work.
6. Build or refresh a task graph from the actual project state and stated goal.
7. Execute the highest-value unblocked task, then run explicit acceptance checks.
8. Record evidence and checkpoint state. A task is complete only when its acceptance criteria are verified.
9. On failure, diagnose, change strategy, retry within policy, or replan. Never repeat an identical failed strategy indefinitely.
10. Respect approval gates for destructive or externally consequential actions.
11. Continue autonomously while useful work remains and the host permits it. On interruption, leave enough persistent state to resume deterministically.
12. Before stopping, report verified progress, unresolved blockers, and the exact next resumable state.

## Completion rule

Do not declare the project complete because the plan is complete. Declare completion only when the project's acceptance criteria are satisfied by current evidence.

## Host neutrality

The protocol does not assume shell, Git, GitHub, network, filesystem, or package-manager access. Use only capabilities actually exposed by the host. When a capability is unavailable, preserve state and continue with independent work rather than fabricating success.

## Canonical repository

When this file is distributed with UASEP, the repository-local implementation and `.uasep/` state are authoritative for project-specific rules and decisions.
