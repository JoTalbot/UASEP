# Migration status on branch `new`

## Done

- [x] Branch `new` from `main`
- [x] TARGET_DESIGN.md
- [x] Unified `runtime/models.py` (Task, ProjectState, …)
- [x] `runtime/graph.py` with validation
- [x] `runtime/store.py`
- [x] `runtime/verify.py`, `runtime/safety.py`
- [x] Canonical `runtime/supervisor.py`
- [x] Schemas: task, state, graph
- [x] `.uasep/graph.json`, updated state/manifest/handoff
- [x] CLI: state, graph, run, resume
- [x] New tests: `test_unified_graph.py`, `test_unified_supervisor.py`

## Remaining (UASEP-UNIFY-003)

- [ ] Make legacy tests import-compatible or delete obsolete tests
- [ ] Thin-wrap or remove `autonomous_loop.py` / `task_graph.TaskNode` dual path
- [ ] Point `StateStore` callers to `Store` or keep adapter shim
- [ ] Full `pytest` green on CI for branch `new`
- [ ] `adapters/local_cli.py`
- [ ] jsonschema validation in `tools/validate_uasep.py`

## Compatibility warning

On this branch, **canonical** APIs are:

- `runtime.models.Task` / `TaskStatus`
- `runtime.graph.TaskGraph`
- `runtime.store.Store`
- `runtime.supervisor.Supervisor`

Files still present from `main` may break if they expect the old `Task` fields (`title`, `BACKLOG`, …) or old `StateStore.to_dict()` shape. Prefer new modules for all new work.
