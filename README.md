# UASEP

**Universal Autonomous Engineering & Self-Maintenance Protocol**

[![UASEP conformance](https://github.com/JoTalbot/UASEP/actions/workflows/tests.yml/badge.svg)](https://github.com/JoTalbot/UASEP/actions/workflows/tests.yml)

Version **3.1.2** — portable protocol for autonomous software engineering across ChatGPT, GitHub-connected agents, local CLIs, sandboxes, IDE agents, and future runtimes.

## Goals

- Start new projects from zero; resume from repository state.
- Discover real capabilities instead of assuming tools exist.
- Plan work as a dependency-aware task graph.
- Implement, test, verify, and persist evidence continuously.
- Cold-resume retries (`task_failures`), multi-agent write-set safety, host-neutral adapters.

## Quick start

```bash
python -m pip install pytest
python -m pytest -q
python -m runtime.cli bootstrap
python -m runtime.cli check
python -m runtime.cli status
python -m runtime.cli plan
python -m runtime.cli migrate
python -m runtime.cli resume
python -m runtime.cli run --task-id demo
```

## Protocol layers

1. **Bootstrap** — short prompt (`bootstrap/UASEP_BOOTSTRAP.md`)
2. **Core** — normative rules under `protocol/`
3. **Adapter** — host mapping (`runtime/host_adapter.py`, `runtime/aios2_adapter.py`)
4. **Project state** — `.uasep/` memory, plans, evidence
5. **Runtime** — reference supervisor, planner, verification

## Design principle

**Discover → Restore → Plan → Execute → Verify → Persist → Replan → Continue.**

Lack of a tool is a constraint to adapt around, not a reason to fabricate results.

## Layout

```text
.uasep/          # project-local instance
protocol/        # normative specs
runtime/         # reference implementation
schemas/         # JSON schemas
tests/           # conformance + integration
bootstrap/       # short prompts
examples/        # workflows
```

## License / contributing

See `CONTRIBUTING.md`. Keep VERSION and `pyproject.toml` aligned. Do not invent CI results.
