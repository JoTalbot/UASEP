# C3.1 Validator Runner

## Purpose

Define the automation layer responsible for executing UASEP validators in a repeatable way.

## Validation flow

```text
Repository State
      |
      v
Validator Runner
      |
      +--> Schema Validator
      +--> Agent Readiness Validator
      +--> Evidence Checker
      +--> Architecture Report
      |
      v
Validation Result
```

## Requirements

- deterministic execution
- explicit status output
- VERIFIED / UNKNOWN / BLOCKED states
- evidence references for successful checks
- failure recording

## Future implementation

The runner can be integrated with CI workflows and local development commands.
