# Handoff

Current state: reference runtime is executable; cycle-budget vs verified-terminal contract is aligned.

Completed: core specification, schemas, planner, supervisor, verification, evidence/checkpoint stores, conformance and integration tests. 103 local pytest cases pass on 3.1.1.

Next: observe GitHub Actions on this commit before claiming CI-verified; persist per-task retry state across process boundaries; continue AIOS2 adoption.

Important: `main` is the stable line. Do not modify the `new` branch. A verified terminal phase must survive a spent cycle budget when no tasks remain.
