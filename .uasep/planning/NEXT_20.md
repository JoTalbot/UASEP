# Next 20 maintenance tasks

Batch: UASEP-MAINT-2026-08-29
Branch: main

| ID | Scope | Files | Dependencies | Risk | Verification | Execution |
|---|---|---|---|---|---|---|
| M42 | Fresh-agent bootstrap drift audit | `bootstrap/`, `AGENTS.md`, readiness protocol | M41 | low | conformance/review | independent |
| M43 | Durable-state schema/narrative cross-check | `.uasep/state/`, `schemas/`, conformance checks | M41 | low | pytest/review | independent |
| M44 | Evidence freshness and uniqueness audit | `.uasep/evidence/`, evidence schema/tests | M41 | low | pytest/review | independent |
| M45 | Ownership fixture lifecycle audit | `.uasep/state/`, ownership schema/fixtures | M41 | M43 | low | pytest/review | dependent |
| M46 | Task-contract lifecycle audit | task contracts + protocol/tests | M41 | M43 | low | pytest/review | dependent |
| M47 | Batch-manifest recovery audit | batch manifests + protocol/tests | M41 | M43 | low | pytest/review | dependent |
| M48 | Skill-to-contract reference audit | `skills/`, `protocol/` | M41 | low | reference audit | independent |
| M49 | Example acceptance-criteria audit | `examples/` | M41 | low | reference audit | independent |
| M50 | Schema fixture completeness audit | `schemas/`, `tests/conformance/fixtures/` | M43 | low | pytest | dependent |
| M51 | Runtime-free active-tree search guard expansion | conformance tests | M42 | low | pytest/search | dependent |
| M52 | Historical-reference boundary documentation audit | docs/knowledge/state | M41 | low | repository search | independent |
| M53 | CI trigger and checkout invariants audit | `.github/workflows/` | M41 | low | workflow review | independent |
| M54 | CI dependency reproducibility audit | `.github/workflows/conformance.yml` | M53 | low | workflow review | dependent |
| M55 | Version-source hierarchy audit | `VERSION`, manifest, protocol/state | M41 | low | pytest/review | independent |
| M56 | Decision/failure evidence linkage audit | `.uasep/knowledge/`, evidence | M44 | low | repository review | dependent |
| M57 | Handoff resumability audit | `.uasep/state/HANDOFF.md`, protocol | M43 | low | review | dependent |
| M58 | Maintenance runbook operational audit | `docs/MAINTENANCE.md` | M42-M57 | low | manual review | dependent |
| M59 | Conformance suite coverage-gap review | `tests/conformance/` | M42-M58 | low | pytest/review | dependent |
| M60 | Fresh canonical CI acceptance pass | `.github/workflows/`, evidence/state | M42-M59 | low | canonical CI | dependent |
| M61 | Durable-state reconciliation after M42-M60 | `.uasep/state/`, planning, evidence | M60 | low | state review + CI | dependent |
| M62 | CI repair, workflow minimization, documentation archive, and hygiene | workflows/tests/docs/state | M61 | medium | pytest + canonical CI | dependent |

## Execution policy

M42-M44, M48-M49, M52-M53, and M55 may be analyzed independently when write sets remain disjoint. Dependent tasks move to later groups. Do not execute overlapping writes in parallel without explicit coordination and updated ownership records.

## Current result

- H01-H20: **VERIFIED / COMPLETE**.
- M11-M20: **VERIFIED / COMPLETE**.
- M21-M23: **VERIFIED / COMPLETE**; canonical runs #94 and #95.
- M24-M30: **VERIFIED / COMPLETE**; canonical run #101.
- M31-M40: **VERIFIED / COMPLETE**; canonical run #108.
- M41: **VERIFIED / COMPLETE**; canonical run #120 at commit `bfb852e6d734b81256f930603c30cac68708c4a5`.
- M42-M61: **COMPLETE / PARTIALLY_VERIFIED at the individual-item level**; reviewed via repository inspection (see `EV-M43-M61-2026-08-29.json` and the M60/M61 CI acceptance in durable state).
- M62: **VERIFIED locally (54/54 conformance tests)**; canonical CI acceptance pending observation — see `EV-UASEP-MAINT-M62-2026-08-30.json`.
- No runtime implementation is introduced.

## Re-scoring rule

Re-score this plan when a concrete defect, drift finding, new acceptance requirement, or materially changed connector capability is discovered. Do not manufacture work merely to keep the maintenance queue busy; humanity has enough paperwork already.
