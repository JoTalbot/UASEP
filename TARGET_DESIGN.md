# UASEP Target Design 3.2

Criteria: **simplicity · unification · necessity**.

## Goal

One working path:

`bootstrap → plan → execute → verify → persist → resume`

## Non-goals (v1 core)

- Multi-agent role framework as MUST
- L5–L7 autonomy as demonstrated levels
- Parallel task execution
- LLM planner inside runtime
- Multiple host adapters before local-cli works

## Canonical data model

### Task

| Field | Type | Notes |
|-------|------|-------|
| id | string | required |
| objective | string | required |
| status | enum | queued, ready, running, blocked, failed, verified, complete, cancelled |
| priority | number | higher = sooner; default 50 |
| dependencies | string[] | hard prerequisites |
| acceptance_criteria | string[] | required (may be empty) |
| risk | enum | low, medium, high, critical |
| owner | string\|null | |
| evidence_ids | string[] | |

**Ready rule:** status in {queued, ready} AND every dependency has status in {verified, complete}.

### ProjectState

Matches `schemas/state.schema.json` and `.uasep/state.json` (same shape).

### Graph persistence

`.uasep/graph.json` — machine source of truth for tasks.

## Single orchestration

`runtime/supervisor.py` is the only public cycle:

- `run_once(project_id)`
- `run_until_idle(project_id, max_cycles=100)`

Semantics: discover-ready → approval → execute → verify → evidence → checkpoint → persist graph+state.

No parallel `AutonomousLoop` API in 3.2 core.

## Module map (target)

```
runtime/
  models.py      # Task, ProjectState, Evidence, Capability, CycleResult
  graph.py       # TaskGraph
  store.py       # state + graph + evidence + checkpoints
  discovery.py   # capabilities
  bootstrap.py   # .uasep init
  verify.py      # VerificationEngine
  safety.py      # ApprovalGate
  supervisor.py  # single loop
  host.py        # HostAdapter protocol + null/local helpers
  conformance.py # MUST checks
  cli.py
```

Legacy modules on `main` remain until migration completes; new code is authoritative on branch `new`.

## Done criteria

1. `uasep bootstrap` creates schema-valid `.uasep/`
2. Dependent tasks run in order via `run`
3. Failed acceptance → failed/blocked, not complete
4. Resume does not redo verified work
5. One Task model, one Supervisor entrypoint
