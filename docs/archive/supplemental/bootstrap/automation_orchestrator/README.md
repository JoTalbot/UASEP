# UASEP Automation Orchestrator

## Purpose

Coordinate repository automation tasks.

## Responsibilities

- receive audit results
- select applicable templates
- coordinate execution order
- track ownership
- persist evidence

## Flow

```
Scanner
  ↓
Planner
  ↓
Generator
  ↓
Verifier
  ↓
State Update
```

The orchestrator does not replace verification; it coordinates it.
