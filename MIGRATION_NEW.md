# Branch `new` — independent cutover

This branch is **not** required to track `main`. Another agent owns `main`.
Ideology on `new`: simplicity, unification, necessity (UASEP CORE + CONFORMANCE).

## Canonical surface

| Module | Role |
|--------|------|
| `runtime/models.py` | Task, ProjectState, Evidence, Capability, CycleResult |
| `runtime/graph.py` | TaskGraph (deps, cycles, ready) |
| `runtime/store.py` | state.json + graph.json + evidence + checkpoints |
| `runtime/supervisor.py` | only orchestration (`run_once`, `run_until_idle`) |
| `runtime/verify.py` | acceptance checks |
| `runtime/safety.py` | ApprovalGate |
| `runtime/discovery.py` | capabilities |
| `runtime/bootstrap.py` | `.uasep` scaffold |
| `runtime/cli.py` | bootstrap, capabilities, check, state, graph, run, resume |

## Redirects (temporary, do not extend)

- `state.StateStore` → `Store`
- `verification` → `verify`
- `approval_gate` → `safety`
- `task_graph.TaskNode` → adapter over `Task`
- `autonomous_loop.AutonomousLoop` → wraps `Supervisor`
- `supervisor_engine.Supervisor` → same class as `supervisor.Supervisor`
- `compatibility.LegacyRuntime` → `Supervisor`

## Policy

- Do not restore dual orchestration semantics.
- Do not add features that are not needed for: discover → plan → execute → verify → persist → resume.
- Prefer deleting dead modules over maintaining parallel APIs.
- Machine truth for tasks: `.uasep/graph.json`.
