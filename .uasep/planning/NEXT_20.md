# Next 20 hardening tasks

Batch: UASEP-HARDEN-2026-08-28
Branch: main

| ID | Scope | Files | Dependencies | Risk | Verification | Execution |
|---|---|---|---|---|---|---|
| H01 | State projection | `.uasep/state/state.json` | state schema | low | JSON Schema | independent |
| H02 | Manifest fixture | `tests/conformance/fixtures/manifest.json` | manifest schema | low | schema validation | independent |
| H03 | State fixture | `tests/conformance/fixtures/state.json` | state schema | low | schema validation | independent |
| H04 | Capabilities fixture | `tests/conformance/fixtures/capabilities.json` | capabilities schema | low | schema validation | independent |
| H05 | Readiness fixture | `tests/conformance/fixtures/readiness.json` | readiness schema | low | schema validation | independent |
| H06 | Ownership fixture | `tests/conformance/fixtures/ownership.json` | ownership schema | low | schema validation | independent |
| H07 | Batch fixture | `tests/conformance/fixtures/batch.json` | batch schema | low | schema validation | independent |
| H08 | Task fixture | `tests/conformance/fixtures/task.json` | task schema | low | schema validation | independent |
| H09 | Evidence fixture | `tests/conformance/fixtures/evidence.json` | evidence schema | low | schema validation | independent |
| H10 | Fixture runner | `tests/conformance/test_fixtures.py` | H02-H09 | low | pytest | dependent on fixtures |
| H11 | Cross-artifact invariants | `tests/conformance/test_all_schemas.py` | H01/H10 | low | pytest | dependent |
| H12 | Runtime-free invariant | `tests/conformance/test_runtime_free.py` | manifest/state/readiness fixtures | low | pytest | independent |
| H13 | Branch invariant | `tests/conformance/test_main_branch.py` | repository contract | low | pytest | independent |
| H14 | Documentation index | `protocol/CONFORMANCE.md` | protocol baseline | low | manual review | independent |
| H15 | Batch execution guide | `docs/BATCH_EXECUTION.md` | batch contract | low | manual review | independent |
| H16 | Failure knowledge | `.uasep/knowledge/FAILURES.md` | observed CI blocker | low | evidence review | independent |
| H17 | Decision record | `.uasep/knowledge/DECISIONS.md` | H01/H16 | low | review | dependent |
| H18 | Durable status sync | `.uasep/state/STATUS.md` | H01/H16 | low | state review | dependent |
| H19 | Handoff sync | `.uasep/state/HANDOFF.md` | H01/H16 | low | handoff review | dependent |
| H20 | Fresh-agent acceptance | `examples/FRESH_AGENT_ACCEPTANCE.md` + evidence | repository-only context | medium | independent fresh session | externally dependent |

## Execution policy

Tasks H02-H09, H12-H15, and H16 can be executed without waiting for each other when write sets remain disjoint. H01 must precede state-dependent checks. H10-H11 and H17-H19 depend on earlier artifacts. H20 requires a genuinely fresh agent/session and cannot be honestly simulated by the current session.

## Batch result

- Planned: 20
- Independently executable now: 13
- Dependent but executable after prerequisites: 6
- Externally dependent: 1 (H20)
- No runtime implementation is introduced.
