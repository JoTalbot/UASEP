# Main runtime hardening

This document records changes made on `main` independently of the experimental `new` branch.

## Branch boundary

- `main` is the stable integration line for this agent.
- `new` is owned by another agent and must not be modified, merged, rebased, or used as a write target here.
- Work from `new` may be reviewed conceptually, but changes are reimplemented independently on `main`.

## Current hardening goals

- deterministic task selection;
- explicit graph invariants;
- bounded failure handling;
- persistent state/checkpoint correctness;
- regression tests before architectural migration.
