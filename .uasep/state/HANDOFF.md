# Handoff — branch `new`

## Policy

Branch `new` is independent of `main`. No compatibility obligation with the other agent’s line.

## Canonical runtime

Supervisor + Store + TaskGraph + unified Task model.
Legacy module names may re-export; they must not introduce a second lifecycle.

## Done

- Unified models / graph / store / supervisor / verify / safety
- CLI: graph, run, resume
- StateStore and AutonomousLoop redirected to unified path
- test_runtime rewritten for unified API

## Next (ideology-aligned)

1. Delete dead legacy files that nothing imports (or only tests that we replace).
2. Strengthen conformance checks to CONFORMANCE.md MUST list.
3. local_cli host adapter for real execute/checks.
4. Keep `.uasep/graph.json` and state honest after every change.
