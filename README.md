# UASEP

**Universal Autonomous Engineering & Self-Maintenance Protocol**

UASEP is a repository-native operating protocol for AI agents working on software projects through chat and GitHub-connected tools.

UASEP is intentionally **runtime-free**. The agent, chat interface, and GitHub connector provide execution. UASEP provides the rules, durable project memory, planning system, coordination protocol, evidence model, and handoff format.

## What UASEP provides

- **Bootstrap** — start or resume work from repository state.
- **Agent instructions** — mandatory behavior for every participating agent.
- **Skills** — reusable workflows for audit, planning, implementation, review, verification, handoff, and recovery.
- **Planning** — backlog, priorities, dependencies, parallelizable work, and acceptance criteria.
- **State** — durable current status independent of chat history.
- **Knowledge** — architectural decisions, discoveries, failures, and lessons learned.
- **Evidence** — explicit records for tests, reviews, CI, and completion claims.
- **Parallel coordination** — compatible write sets, ownership, conflict avoidance, and integration rules.
- **Self-maintenance** — controlled improvement of protocol and project documentation.

## Runtime-free architecture

```text
Chat + AI agent
      │
      │ GitHub Connector
      ▼
Git repository
  source + protocol + state + plans + evidence
```

There is no UASEP daemon, CLI, Python runtime, scheduler, database, or agent supervisor to install.

## Repository layout

```text
AGENTS.md
skills/
docs/
protocol/
.uasep/
  manifest.yaml
  planning/
  state/
  knowledge/
  evidence/
bootstrap/
examples/
adapters/
schemas/
tests/
```

## Standard agent cycle

**Discover → Restore → Audit → Plan → Execute → Verify → Integrate → Persist → Handoff → Continue**

Agents must inspect the repository before acting, use durable state instead of relying on chat history, make reversible changes where practical, and never claim work that has not been verified.

## Parallel work

Independent tasks may be analyzed and executed in batches when dependencies and write sets do not conflict. Every consequential task must have explicit ownership, acceptance criteria, verification status, and recorded evidence.

## Truth model

- `VERIFIED` — directly supported by evidence.
- `PARTIALLY_VERIFIED` — some required evidence exists, but verification is incomplete.
- `UNKNOWN` — insufficient evidence.
- `FAILED` — evidence demonstrates that the claim or acceptance criterion failed.

Unknown is never silently promoted to verified.

## Start here

1. Read `AGENTS.md`.
2. Read applicable `skills/` workflows.
3. Read `.uasep/state/HANDOFF.md` and `.uasep/state/PROJECT_STATE.md`.
4. Read `.uasep/planning/MASTER_PLAN.md` and `.uasep/planning/BACKLOG.md`.
5. Inspect the actual repository and current Git history.
6. Establish readiness and ownership before consequential edits.
7. Continue from durable repository state rather than chat memory.
