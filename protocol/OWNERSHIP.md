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

## Branch lifecycle

Branches are part of the shared coordination state and accumulate debt when
left behind.

1. **One task lineage, one branch.** Short-lived work branches (for example
   `batch/<n>-<slug>`) must be deleted after their work lands.
2. **Never force-push or rewrite shared branches.** Integration conflicts are
   resolved against the current target branch.
3. **Merged does not mean ancestry.** Rebase and squash merges break
   `merge-base --is-ancestor` checks: a merged branch is often *not* an
   ancestor of the target. Verify inclusion by patch equivalence
   (`git cherry <target> <branch>`) or content inspection before judging a
   branch stale.
4. **Delete provably-merged branches.** A branch whose commits are all
   patch-equivalent to the target can be deleted; git history preserves the
   content.
5. **Preserve unique histories deliberately.** For branches with work not in
   the target that must be kept, create an explicit `archive/<name>` tag (or
   close them with a recorded decision) instead of leaving the branch ref
   dangling forever.
6. **Record bulk cleanup as a task.** Mass branch deletion is a consequential
   operation: claim ownership, verify each branch, record evidence, and
   summarize what was deleted and what was preserved.
