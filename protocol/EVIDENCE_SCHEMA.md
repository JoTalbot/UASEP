# UASEP Evidence Schema

Evidence records what was actually observed. They MUST NOT convert an intention or attempted action into a success claim.

## Required fields

- `evidence_id`
- `task_id`
- `timestamp`
- `agent`
- `operation`
- `scope`
- `result`: `VERIFIED`, `PARTIALLY_VERIFIED`, `UNKNOWN`, or `FAILED`.
- `source`: repository file, GitHub operation result, test/CI result, or other explicitly identified source.
- `observed`: concise factual observation.

## Optional fields

- commit SHA;
- changed files;
- verification command/check;
- limitations;
- related decision/task IDs.

## Rules

1. Evidence describes observation, not expectation.
2. A successful file update proves the repository update operation succeeded; it does not prove unrelated tests or external effects.
3. Absence of evidence is not evidence of success.
4. If the tool result is ambiguous, use `UNKNOWN`.
5. Verification evidence should identify exactly what was checked.
6. Historical search results are provenance, not evidence that a retired artifact exists in the active tree.

## Minimal template

```text
EVIDENCE_ID: EV-XXX
TASK_ID: UASEP-TASK-XXX
TIMESTAMP: ...
AGENT: ...
OPERATION: ...
SCOPE: ...
RESULT: VERIFIED
SOURCE: ...
OBSERVED: ...
COMMIT: ...
LIMITATIONS: NONE
```
