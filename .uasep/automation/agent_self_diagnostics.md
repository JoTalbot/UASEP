# Agent Self-Diagnostics

## Purpose

Define pre-action and post-action self-checks for UASEP agents.

## Diagnostics flow

```
Agent Start
    |
    v
Context Check
    |
    v
Ownership Check
    |
    v
Task Contract Check
    |
    v
Evidence Check
    |
    v
Completion Review
```

## Checks

- AGENTS.md availability
- Project state availability
- Handoff continuity
- Task contract presence
- Verification plan presence
- Evidence attachment
- Final status consistency

## Status model

- READY
- UNKNOWN
- BLOCKED

## Rule

Self-diagnostics must run before claiming completion.
