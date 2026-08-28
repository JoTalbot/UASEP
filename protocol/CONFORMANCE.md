# UASEP Conformance Specification

Version: 3.1

## Purpose

UASEP is a repository-native operating protocol for AI agents working through chat and connected repository tools. Conformance describes agent behavior and durable project artifacts; it does not require a UASEP runtime.

## Required agent behavior

A conformant agent MUST:

1. Discover the actual repository, branch, available tools, and relevant instructions before consequential work.
2. Restore project context from durable UASEP state before acting.
3. Represent meaningful work as tasks with objective, scope, dependencies, acceptance criteria, owner, risk, and verification plan.
4. Inspect actual files before proposing or applying changes.
5. Execute only actions supported by the capabilities actually available in the current session.
6. Verify consequential changes with proportionate evidence.
7. Persist decisions, failures, status, evidence, and handoff information in repository artifacts.
8. Detect repeated failures, no-op progress, and conflicting ownership, then change strategy or stop safely.
9. Distinguish VERIFIED, PARTIALLY_VERIFIED, UNKNOWN, and FAILED claims.
10. Protect destructive or irreversible operations with explicit approval and a recoverable checkpoint where practical.
11. Leave the repository in a state another agent can understand and continue without hidden chat history.
12. Never claim a tool action, test, CI result, commit, or external effect without evidence.

## Completion invariant

A task MUST NOT be marked `done` solely because an implementation attempt was made. Acceptance criteria must be satisfied and evidence recorded.

## Recovery invariant

After interruption, durable project artifacts MUST identify the current objective, current task, completed work, unverified work, blockers, relevant decisions, changed files/commits, and next action.

## Parallel-work invariant

Tasks may be analyzed in parallel, but execution may be parallel only when their write sets and dependencies are compatible. Conflicting work requires explicit coordination.

## Connector invariant

GitHub-connected tools are capabilities of the current agent session, not assumptions of the protocol. The agent MUST inspect and use only the tools actually available.

## Portability invariant

UASEP state and instructions MUST remain understandable through ordinary repository files and MUST NOT depend on hidden chat history or a specific AI vendor.
