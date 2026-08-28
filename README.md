# UASEP

**Universal Autonomous Engineering & Self-Maintenance Protocol**

UASEP is a repository-native operating protocol for AI agents working on software projects through chat and GitHub-connected tools.

UASEP is intentionally **runtime-free**. The agent, chat interface, and GitHub connector provide execution. UASEP provides the rules, durable project memory, planning system, coordination protocol, evidence model, and handoff format.

## What UASEP provides

- **Bootstrap** — start or resume work from a short instruction.
- **Agent instructions** — mandatory behavior for every participating agent.
- **Skills** — reusable workflows for audit, planning, implementation, review, verification, handoff, and recovery.
- **Planning** — backlog, priorities, dependencies, parallelizable work, and acceptance criteria.
- **State** — durable current status independent of chat history.
- **Knowledge** — architectural decisions, discoveries, failures, and lessons learned.
- **Evidence** — explicit records for tests, reviews, CI, and other completion claims.
- **Parallel coordination** — compatible write sets, ownership, conflict avoidance, and integration rules.
- **Self-maintenance** — agents continuously improve the protocol and project documentation when useful.

## Runtime-free architecture

```text
┌──────────────────────────────┐
│ Chat + AI agent              │
│ reasoning / planning / work  │
└──────────────┬───────────────┘
               │ GitHub Connector
               ▼
┌──────────────────────────────┐
│ Git repository               │
│ source + UASEP protocol      │
│ state + plans + knowledge    │
│ evidence + handoffs          │
└──────────────────────────────┘
```

There is no UASEP daemon, CLI, Python runtime, scheduler, database, or agent supervisor to install.

## Repository layout

```text
AGENTS.md                  # entry instructions for every agent
skills/                    # reusable agent workflows
docs/                      # protocol guides and operational reference
protocol/                  # normative rules
.uasep/
├── manifest.yaml          # protocol/project declaration
├── planning/              # backlog and master plan
├── state/                 # current state and handoff
├── knowledge/             # decisions, failures, discoveries
└── evidence/              # verification records
bootstrap/                 # minimal bootstrap prompts
examples/                  # usage examples
adapters/                  # environment-specific guidance
```

## Standard agent cycle

**Discover → Restore → Audit → Plan → Execute → Verify → Integrate → Persist → Handoff → Continue**

Agents must inspect the repository before acting, use durable state instead of relying on chat history, make reversible changes where practical, and never claim work that has not been verified.

## Parallel work

Independent tasks may be analyzed and executed in batches when their dependencies and write sets do not conflict. Every batch must record ownership, acceptance criteria, verification status, and any remaining blockers.

## Truth model

- `VERIFIED` — directly supported by evidence.
- `INFERRED` — reasonable conclusion not directly verified.
- `UNKNOWN` — insufficient evidence.
- `BLOCKED` — cannot proceed safely or completely.

Unknown is never silently promoted to verified.

## Start here

1. Read `AGENTS.md`.
2. Read the applicable files in `skills/`.
3. Read `.uasep/state/HANDOFF.md` and `.uasep/state/PROJECT_STATE.md`.
4. Read `.uasep/planning/MASTER_PLAN.md` and `.uasep/planning/BACKLOG.md`.
5. Inspect the actual repository and current Git history.
6. Continue from the recorded state rather than restarting from chat memory.
