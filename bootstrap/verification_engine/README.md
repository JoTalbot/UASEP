# UASEP Verification Engine

## Purpose

Validate changes produced by automation before they are considered complete.

## Checks

- CI status
- workflow validity
- generated files
- repository consistency
- evidence records

## Flow

```
Changes
  ↓
Verification Engine
  ↓
Evidence
  ↓
VERIFIED / FAILED
```

Unknown results remain UNKNOWN until evidence exists.
