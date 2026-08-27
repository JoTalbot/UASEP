# Agent Coordination Protocol

Agents are interchangeable workers under a supervisor or equivalent coordinator.

## Roles

Typical roles include researcher, architect, developer, tester, security reviewer, DevOps, documentation, and release/reviewer. Roles are capabilities, not permanent identities.

## Coordination

Each delegated task must define objective, scope, inputs, outputs, acceptance criteria, dependencies, and ownership. Agents must not silently overwrite shared work owned by another active task.

## Parallel work

Run tasks in parallel only when their write sets and dependencies are compatible. Integrate results through explicit verification and conflict checks.

## Contracts

Prefer structured task contracts over transferring large conversational context. Report facts, changes, evidence, blockers, and recommended next actions.

## Supervisor

A supervisor prioritizes work, allocates agents, detects conflicts, collects evidence, and decides the next task. The supervisor must remain accountable for overall project state.
