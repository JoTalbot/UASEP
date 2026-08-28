# Handoff (branch `new`)

## Current state

Target-design 3.2 unified path landed on branch `new`:

- `runtime/models.py` — single Task / ProjectState / Evidence / CycleResult
- `runtime/graph.py` — TaskGraph with cycle/self-dep/unknown-dep validation
- `runtime/store.py` — state + graph + evidence log + checkpoints
- `runtime/supervisor.py` — single orchestration (`run_once` / `run_until_idle`)
- `runtime/verify.py`, `runtime/safety.py`
- schemas aligned: task, state, graph
- `.uasep/graph.json` is machine source of truth for tasks

## Completed

- UASEP-UNIFY-001, UASEP-UNIFY-002 (design + core modules pushed)

## Next

- UASEP-UNIFY-003: wire CLI, thin-wrap or delete legacy dual path, full CI green
- local_cli adapter
- schema validation in `tools/validate_uasep.py`

## Important

Legacy files from `main` (AutonomousLoop, TaskNode, old StateStore shape) may still exist for compatibility. **Canonical API on this branch is Supervisor + Store + TaskGraph.**
