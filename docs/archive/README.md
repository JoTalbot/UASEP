# Archive

This directory contains **non-normative, archived documentation**. Nothing here
is part of the UASEP protocol, and nothing here authorizes executable
infrastructure.

## Why this archive exists

During the 2026-08-28/30 development sprints, the repository accumulated
documentation from ~90 self-generated "C-cycles" plus retired runtime
(AIOS2-era) architecture concepts. That material:

- duplicated the same topics many times over (knowledge engines appeared in
  cycles C10, C18, C26, C35, C50; similar repeats across economy, ethics,
  energy, prediction, trust, and others),
- was never requested by a concrete defect, drift finding, or acceptance
  requirement,
- and blurred the boundary between the adopted runtime-free protocol and
  aspirational architecture essays.

Maintenance task **M62** (2026-08-30) moved it here so that `.uasep/` holds
only canonical durable state and the active tree matches the layout declared
in the README. The project's own rule applies going forward: *do not
manufacture work merely to keep the maintenance queue busy.*

## Contents

- `durable-state/` — topic documents that had accumulated inside `.uasep/`
  (one subdirectory per former topic). The canonical durable-state
  directories (`state/`, `planning/`, `knowledge/`, `evidence/`,
  `decisions/`) were kept in place; only their `cNN_*.md` cycle documents
  were archived.
- `supplemental/` — the former top-level `runtime/`, `control_plane/`,
  `integration/`, `intelligence/`, and `uasep/` (C81–C90, runtime
  architecture, bootstrap-module designs) trees.

## Policy

- Archived documents are provenance only. They are not roadmap stages and
  are not maintained.
- New documents enter the active tree only when a concrete defect, drift
  finding, or acceptance requirement justifies them (see
  `protocol/SELF_MAINTENANCE.md`).
- Deleting archived material entirely is acceptable once its provenance value
  is exhausted; git history preserves everything.
