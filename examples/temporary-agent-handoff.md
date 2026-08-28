# Temporary-agent handoff

When an agent session ends, leave the next agent able to resume without chat history.

## Required artifacts

1. `.uasep/state.json` — phase, completed, blockers, task_failures
2. `.uasep/state/HANDOFF.md` — short next actions
3. `.uasep/planning/BACKLOG.md` — prioritized remaining work
4. `.uasep/evidence/` — what was verified and how

## Handoff checklist

- [ ] No invented CI/test results
- [ ] Open PRs linked or merged
- [ ] Blockers explicit
- [ ] Highest-value next task identified
- [ ] Write sets of in-flight work recorded if parallel agents used
