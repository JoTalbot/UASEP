# Automatic Evidence Collection

## Purpose
Define a controlled process for collecting verification artifacts.

## Collection Flow

```
Task Result
    ↓
Artifact Discovery
    ↓
Evidence Record
    ↓
Validation
    ↓
State Update
```

## Checks

- Link evidence to claims
- Preserve timestamps and source references
- Mark unavailable evidence as UNKNOWN
- Prevent VERIFIED status without artifacts

## Status Model

- VERIFIED: evidence collected and validated
- UNKNOWN: evidence unavailable
- BLOCKED: collection prevented by dependency
