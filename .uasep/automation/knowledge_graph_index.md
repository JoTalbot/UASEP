# Knowledge Graph Index

## Purpose
Create a linked model connecting UASEP knowledge artifacts.

## Nodes

- Decisions
- Lessons Learned
- Failures
- Tasks
- Evidence
- State records

## Relations

```
Decision -> Evidence
Failure -> Lesson
Task -> Artifact
Artifact -> Verification
Lesson -> Prevention
```

## Requirements

- Preserve traceability
- Avoid duplicate knowledge
- Keep references explicit
- Support automated navigation

## Status Model

- VERIFIED
- UNKNOWN
- BLOCKED
