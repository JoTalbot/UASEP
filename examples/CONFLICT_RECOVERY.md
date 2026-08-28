# Conflict and Recovery Example

## Conflict

Agent A owns `docs/api.md`. Agent B discovers that its task also requires changing that file.

B must not silently edit the overlap.

1. Stop consequential edits to the overlap.
2. Inspect A's ownership claim and task dependency.
3. Decide whether to partition scope, serialize the work, or coordinate a shared change.
4. Record the decision and updated ownership.
5. Resume only within the reconciled write set.

## Connector failure

An agent attempts a repository update and the connected GitHub action fails.

The agent records the operation as `FAILED` when failure is evidenced, or `UNKNOWN` when the outcome cannot be established. It must not claim that the change or commit occurred. Independent safe work may continue.

## Interrupted work

If the chat ends after partial edits, the next agent reconstructs state from the repository. It verifies actual files and commits, checks ownership, and compares them with `STATUS.md` and `HANDOFF.md` before continuing.

## Repeated failure

If the same operation fails repeatedly without new information, stop retrying unchanged. Reclassify the blocker, change strategy if safe, or leave a durable blocker for the next agent.

## Acceptance

Recovery is complete only when ownership is unambiguous, actual repository state is reconciled with durable state, and the next safe action is recorded.
