# Handoff

Current state: reference runtime is executable; cycle-budget vs verified-terminal contract is aligned; per-task failure counts persist across process restarts.

Completed: core specification, schemas, planner, supervisor, verification, evidence/checkpoint stores, conformance and integration tests, cold-resume of task_failures (3.1.2). Local pytest: 104 passed.

Next: observe GitHub Actions on this commit before claiming CI-verified; add formal versioning/migration spec; continue AIOS2 adoption.

Important: `main` is the stable line. Do not modify the `new` branch. A verified terminal phase must survive a spent cycle budget when no tasks remain. Failure counts must survive cold process restart.
