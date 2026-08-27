# UASEP Autonomous Development Contract

This document is the normative contract for autonomous project development.

## Lifecycle

An implementation MUST:

1. Discover the project and execution environment.
2. Bootstrap a new project or resume an existing UASEP state.
3. Build or recover a task plan from the current project state.
4. Execute only through declared host capabilities.
5. Verify completed work using explicit acceptance evidence.
6. Persist evidence and checkpoints before advancing durable progress.
7. Recover after interruption without repeating verified work.
8. Re-plan when execution or verification invalidates the current plan.
9. Apply safety and approval boundaries to privileged or destructive actions.
10. Continue while actionable work remains and stop only on verified completion, an explicit blocker, or an unrecoverable safety boundary.

## Completion

A project MUST NOT be reported as complete merely because an executor returned success. Completion requires the applicable verification checks to pass and durable state/evidence to be recorded.

## Failure and recovery

Transient failures SHOULD be retried with bounded backoff or replanned. Repeated stagnation MUST become an explicit blocker rather than an infinite loop. A restart MUST consume persisted state and preserve verified progress.

## Host neutrality

The contract is independent of the host environment. GitHub-connected ChatGPT, local CLI agents, temporary sandboxes, and other hosts provide capabilities through the same adapter boundary.

## Self-maintenance

When the project being developed is UASEP itself, the same lifecycle applies recursively. Changes to the protocol/runtime MUST be verified by the repository's conformance and integration gates before being treated as durable improvements.
