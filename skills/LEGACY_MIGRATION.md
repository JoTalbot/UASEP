# Skill: Legacy Migration

Migrate an existing agent-coordination system (a homegrown status file,
`.agents/` directory, or older UASEP layout) onto the current UASEP artifact
tree without losing knowledge or breaking ongoing work.

## When to use

- The project already has agent instructions, status files, skills, or memory
  that predate UASEP or an older UASEP version.
- Two coordination systems are about to coexist (never leave both active).

## Procedure

1. **Inventory the legacy system.** List every artifact: instructions,
   status, roles, skills, memory, manifests. Note what references them.
2. **Verify, then trust.** Treat every legacy status claim as `UNKNOWN`
   until checked against git history and the actual tree. Legacy status
   files drift; the repository is the source of truth. In particular,
   rebase merges break branch-ancestry checks — verify "is this work already
   in main?" by patch equivalence (`git cherry`) or content inspection, not
   `merge-base --is-ancestor`.
3. **Map and migrate.** Standard mapping:

   | Legacy | UASEP destination |
   |---|---|
   | agent instructions / protocol rules | `AGENTS.md` (project contract) |
   | status / current work | `.uasep/state/STATUS.md`, `state.json`, `HANDOFF.md` |
   | roles | folded into `AGENTS.md` responsibilities |
   | skills | `skills/` (one workflow per skill) |
   | memory / lessons | `.uasep/knowledge/LESSONS.md`, `FAILURES.md` |
   | decisions / ADRs | `.uasep/decisions/` |
   | old manifest | `.uasep/manifest.yaml` (current schema) |

4. **Preserve project-specific rules.** Domain rules (branch workflow,
   architecture constraints, regression coverage requirements) carry over
   into `AGENTS.md` and the local `protocol/README.md` norms — adoption must
   not weaken project discipline.
5. **Retire, do not duplicate.** Record the migration as an ADR
   (`.uasep/decisions/`), then remove the legacy directory. Git history
   preserves it; two live coordination systems guarantee drift.
6. **Record the baseline and evidence.** Before touching anything, run the
   project's test suite and record it (`.uasep/evidence/`); after migration,
   re-run and compare. Machine-readable records must validate against the
   current schemas.
7. **Update references.** Grep for legacy paths in docs and CI; update or
   supersede them.

## Completion

Migration is done when the legacy tree is gone, every piece of live content
has a new home, the test baseline is unchanged, and a fresh agent can
continue from the new artifacts alone.
