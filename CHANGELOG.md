# Changelog

## 3.2.0-new — Unification branch (`new`)

- Independent of `main` (no compatibility obligation).
- Single Task / ProjectState / TaskGraph / Store / Supervisor.
- Mandatory verification before complete; approval gate; failure_count → blocked.
- Persistent `.uasep/graph.json` + honest state/handoff.
- `LocalCliAdapter` with touch/write/cmd and file_exists/file_contains/cmd checks.
- CLI: bootstrap, capabilities, check, state, graph, run, resume (local_cli when importable).
- Bootstrap creates state.json + graph.json.
- Dead modules removed progressively; validator scoped to unified tests.
- Redirects: StateStore, AutonomousLoop, task_graph.TaskNode, verification, approval_gate.

## 3.1.0 — Initial reference specification (main lineage)

- Protocol docs, schemas, early dual runtime paths.
