# Main Engineering Rules

This document defines the working boundary for the stable `main` line.

## Branch isolation

- This workstream writes only to `main`.
- The `new` branch is owned by another AI agent and is an independent development line.
- Do not merge, rebase, cherry-pick, reset, or otherwise modify `new` from this workstream.
- Ideas observed on `new` may be independently reimplemented on `main` only when they improve the main contract.

## Runtime invariants

Every execution path must preserve:

1. deterministic task selection;
2. dependency validity;
3. bounded failure/retry behavior;
4. verification before completion;
5. durable state and checkpoint persistence;
6. safe recovery after interruption;
7. explicit blockers instead of silent stalls;
8. regression coverage for changed behavior.

## Release discipline

A release gate must never be marked complete merely because documentation says it is complete. Claims about CI, tests, validation, or compatibility require current durable evidence from the repository or CI.

## Architecture evolution

The stable line may evolve independently. Do not force convergence with experimental branches. Prefer small, backwards-compatible runtime hardening steps followed by tests and validation.
