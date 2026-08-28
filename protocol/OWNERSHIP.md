# UASEP Ownership and Lease Protocol

Ownership prevents concurrent agents from silently modifying the same scope.

## Claim

Before consequential edits, an agent records:

- task ID;
- owner/session identifier;
- branch;
- explicit write set;
- claimed-at timestamp;
- expected completion or review point;
- dependencies;
- status.

The write set should name files or bounded directories. Broad claims such as "entire repository" should be avoided when narrower ownership is possible.

## Rules

1. One active owner per overlapping write set.
2. Disjoint write sets may proceed concurrently.
3. A dependency does not become ownership merely because it is referenced.
4. Read-only inspection does not require exclusive ownership.
5. Ownership does not authorize changes outside the declared write set.
6. Before expanding a write set, reconcile ownership again.

## Lease

Ownership is a coordination claim, not a permanent lock. Agents should refresh or close the claim through durable state when work continues across sessions.

A claim with no recent evidence may be stale. Do not silently take over a stale claim; record the reconciliation and either release, renew, or coordinate it.

## Completion

On completion, record the resulting commit/change, verification evidence, unresolved risks, and release/transfer of ownership.

## Collision handling

If two agents discover overlapping active claims:

1. stop consequential edits to the overlap;
2. identify the owners and tasks;
3. compare dependencies and acceptance criteria;
4. choose serialization, scope partitioning, or explicit coordination;
5. record the decision before resuming.

If coordination is unavailable, the safer default is to remain `BLOCKED` rather than overwrite another agent's work.
