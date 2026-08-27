# UASEP

**Universal Autonomous Engineering & Self-Maintenance Protocol**

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
5. **Runtime**: optional executable implementation such as an AIOS2 supervisor.

## Repository layout

```text
.uasep/
├── manifest.yaml
├── state.json
├── capabilities.json
├── CORE.md
├── CAPABILITIES.md
├── EXECUTION.md
├── SAFETY.md
├── QUALITY.md
├── MEMORY.md
├── AGENTS.md
├── SELF_MAINTENANCE.md
├── state/
├── planning/
├── knowledge/
└── evidence/
```

The `.uasep/` directory is the project-local instance. This repository is the protocol source of truth and reference specification.

## Bootstrap

Use the short universal bootstrap from `bootstrap/UASEP_BOOTSTRAP.md`. It is intentionally small. The full protocol is loaded from the project or this repository when available.

## Design principle

**Discover → Restore → Plan → Execute → Verify → Persist → Replan → Continue.**

Lack of a specific tool is a constraint to adapt around, not a reason to fabricate results or stop prematurely.
