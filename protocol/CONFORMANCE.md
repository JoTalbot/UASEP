# UASEP Conformance Specification

Version: 3.1

## Purpose

A UASEP implementation is conformant when it preserves the protocol invariants below, regardless of runtime or host environment.

## Required capabilities

The implementation MUST:

1. Discover the current environment and available capabilities.
2. Detect whether a project exists and whether a UASEP instance exists.
3. Bootstrap missing UASEP project state without destroying existing project data.
4. Restore project state before making consequential changes.
5. Represent work as tasks with status, priority, dependencies, and acceptance criteria.
6. Execute only actions supported by actual capabilities.
7. Verify consequential work with appropriate evidence.
8. Persist state, decisions, failures, and handoff information.
9. Detect repeated failures and change strategy rather than looping indefinitely.
10. Distinguish VERIFIED, PARTIALLY_VERIFIED, UNKNOWN, and FAILED claims.
11. Protect destructive or irreversible operations with checkpoints and approval rules.
12. Resume safely after interruption.

## Completion invariant

A task MUST NOT be marked `done` solely because an implementation attempt was made. The implementation must satisfy its acceptance criteria and have proportionate evidence.

## Recovery invariant

After interruption, the implementation MUST be able to reconstruct the active task, repository state, last known evidence, blockers, and next action from persistent project artifacts.

## Capability invariant

An implementation MUST NOT claim access to a capability merely because the protocol describes it. Capabilities are runtime facts and must be discovered or explicitly configured.

## Autonomy invariant

The implementation SHOULD continue through safe, bounded engineering actions without requesting unnecessary human confirmation. Human approval is required when policy, permissions, security, destructive actions, or ambiguous product decisions require it.

## Interoperability invariant

Protocol state MUST remain portable. A conformant implementation should be able to hand off work to another conformant implementation without relying on hidden chat history.
