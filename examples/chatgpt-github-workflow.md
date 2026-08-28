# ChatGPT + GitHub workflow (UASEP)

## Setup
1. Connect GitHub to the agent host.
2. Open repo `JoTalbot/UASEP` (or target project).
3. Paste the short bootstrap (`UASEP_BOOTSTRAP.md` / `bootstrap/SHORT_PROMPT.md`).

## Loop
1. Discover capabilities (GitHub tools, no assumed shell).
2. Load `.uasep/state.json`, HANDOFF, BACKLOG — prefer repo state over chat.
3. Pick highest-value unblocked task; implement via GitHub file APIs / PRs.
4. Run acceptance: local pytest if shell available, else CI on PR.
5. Record evidence under `.uasep/evidence/`; update state/handoff.
6. Open PR → wait for green Actions → merge.

## Rules
- Never invent CI results.
- Cold resume uses persisted `task_failures` and completed_tasks.
- Destructive ops need explicit approval gate.
- Stop only on verified completion or explicit blocker.
