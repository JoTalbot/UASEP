# Task status mapping

Runtime `TaskStatus` (models.py) and schema `task.schema.json` use different vocabularies on purpose until a MINOR alignment release.

| Runtime | Schema (approx) |
|---------|-----------------|
| backlog | queued |
| ready | ready |
| in_progress | running |
| blocked | blocked |
| failed | failed |
| done | verified / complete |

Adapters and external planners SHOULD map explicitly; do not assume string equality.
