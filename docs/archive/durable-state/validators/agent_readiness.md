# Agent Readiness Validator

## Purpose

Validate that an agent has enough context before making repository changes.

## Checks

- AGENTS.md available
- required skills discovered
- project state restored
- handoff reviewed
- ownership established
- task contract created
- verification plan defined

## Result States

- READY
- BLOCKED
- UNKNOWN

A missing verification signal must not be reported as READY.
