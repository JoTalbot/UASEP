# Next 20 maintenance tasks

Batch: UASEP-MAINT-2026-08-28
Branch: main

| ID | Scope | Files | Dependencies | Risk | Verification | Execution |
|---|---|---|---|---|---|---|
| M21 | Durable-state narrative consistency | `tests/conformance/test_protocol_invariants.py` | current state artifacts | low | pytest | independent |
| M22 | Project-state synchronization | `.uasep/state/PROJECT_STATE.md` | acceptance + CI evidence | low | state review | independent |
| M23 | Maintenance-plan rescore | `.uasep/planning/NEXT_20.md` | M21-M22 findings | low | plan review | dependent |
| M24 | Evidence index consistency | `.uasep/evidence/` + conformance checks | evidence schema | low | pytest/review | independent |
| M25 | Bootstrap artifact index | `bootstrap/` + conformance checks | bootstrap protocol | low | pytest/review | independent |
| M26 | Skill inventory consistency | `skills/` + documentation | skill contract | low | repository review | independent |
| M27 | Example-to-protocol references | `examples/` | protocol docs | low | link/reference audit | independent |
| M28 | Schema-to-fixture coverage | `schemas/` + `tests/conformance/fixtures/` | M24 | low | pytest | independent |
| M29 | State-to-manifest version guard | conformance tests | manifest/state schema | low | pytest | independent |
| M30 | Runtime-free active-tree guard | conformance tests | runtime-free contract | low | pytest | independent |
| M31 | CI trigger/read-only policy audit | `.github/workflows/conformance.yml` | CI contract | low | workflow review | independent |
| M32 | CI evidence freshness guidance | protocol/docs | M31 | low | documentation review | dependent |
| M33 | Stale runtime-reference audit | active protocol/docs | runtime-free architecture | low | repository search | independent |
| M34 | Ownership-lease fixture coverage | `tests/conformance/fixtures/` + tests | ownership schema | low | pytest | independent |
| M35 | Evidence status vocabulary coverage | evidence schema + tests | evidence contract | low | pytest | independent |
| M36 | Handoff completeness guard | state/handoff conformance | handoff contract | low | pytest | independent |
| M37 | Status completeness guard | `.uasep/state/STATUS.md` + tests | durable state | low | pytest/review | independent |
| M38 | Acceptance evidence linkage | acceptance example + evidence | M24 | low | review | dependent |
| M39 | Decision/failure cross-reference audit | `.uasep/knowledge/` | evidence records | low | repository review | independent |
| M40 | Maintenance runbook | `docs/MAINTENANCE.md` | M21-M39 | low | manual review | dependent |

## Execution policy

M21, M22, M24-M31, M33-M35, M36-M39 may be analyzed independently when their write sets remain disjoint. M23 depends on the first findings. M32, M38, and M40 depend on earlier artifacts. Do not reopen completed H01-H20 or M11-M20 without a concrete defect, drift finding, or new acceptance requirement.

## Current result

- H01-H20: **VERIFIED / COMPLETE** based on repository evidence and recorded acceptance evidence.
- M11-M20: **VERIFIED / COMPLETE**; protocol-invariant conformance coverage is verified by canonical main-branch run #72.
- M21-M23: **VERIFIED / COMPLETE**; verification gate satisfied by canonical runs #94 and #95.
- M24-M30: **VERIFIED / COMPLETE**; verification gate satisfied by canonical run #101.
- M31-M40: **VERIFIED / COMPLETE**; verification gate satisfied by canonical run #108.
- No active maintenance batch.
- No runtime implementation is introduced.
