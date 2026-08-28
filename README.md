# UASEP

**Universal Autonomous Engineering & Self-Maintenance Protocol**

> Branch **`new`** (3.2.0-new): unification — one Task model, persistent TaskGraph, single Supervisor. See [TARGET_DESIGN.md](TARGET_DESIGN.md) and [MIGRATION_NEW.md](MIGRATION_NEW.md).

UASEP is a portable protocol for autonomous software engineering across ChatGPT, GitHub-connected agents, local CLIs, sandboxes, IDE agents, and future agent runtimes.

## Goals

- Start new projects from zero.
- Resume existing projects from repository state.
- Discover real capabilities instead of assuming tools exist.
- Plan work as a dependency-aware task graph.
- Implement, test, review, verify, integrate, and document continuously.
- Preserve state so another agent can resume without chat history.
- Recover from failures and avoid repeated dead ends.
- Maintain evidence for important completion claims.
- Continuously maintain and improve both the project and its engineering process.

## Protocol layers

1. **Bootstrap**: a short prompt starts the protocol.
2. **Core**: normative rules shared by all environments.
3. **Adapter**: maps abstract capabilities to the current environment.
4. **Project state**: persistent memory, plans, tasks, decisions, failures, and evidence.
5. **Runtime**: executable implementation (canonical entry: `runtime.supervisor.Supervisor` on branch `new`).

## Canonical runtime (branch `new`)

```text
runtime/models.py      # Task, ProjectState, Evidence
runtime/graph.py       # TaskGraph (+ cycle checks)
runtime/store.py       # state.json + graph.json + evidence + checkpoints
runtime/supervisor.py  # run_once / run_until_idle
runtime/cli.py         # bootstrap | capabilities | check | state | graph | run | resume
```

Machine task source of truth: `.uasep/graph.json`.

## Bootstrap

Use the short universal bootstrap from `bootstrap/SHORT_PROMPT.md` / `bootstrap/UASEP_BOOTSTRAP.md`.

## Design principle

**Discover → Restore → Plan → Execute → Verify → Persist → Replan → Continue.**

Lack of a specific tool is a constraint to adapt around, not a reason to fabricate results or stop prematurely.
