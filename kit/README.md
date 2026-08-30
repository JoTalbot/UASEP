# UASEP Conformance Kit

A portable, dependency-light pytest suite that validates a repository's UASEP
artifacts against the published JSON schemas. Drop it into any project that
has adopted UASEP and get continuous conformance checking in CI.

## What it validates

- `.uasep/manifest.yaml` — structure and schema conformance (`protocol`,
  `protocol_version`, `uasep_runtime: NONE`, …)
- `.uasep/state/state.json` — schema conformance and consistency with the
  manifest (protocol, version, project state)
- Required durable artifacts — `AGENTS.md`, `.uasep/state/{STATUS,PROJECT_STATE,HANDOFF}.md`,
  `.uasep/planning/`, `.uasep/knowledge/`, `.uasep/evidence/`
- Every `TASK_*.json`, `OWNERSHIP_*.json`, and evidence record in
  `.uasep/` — schema conformance, unique evidence IDs

## Install

1. Copy `kit/uasep/` into the adopting repository as `tests/uasep/`:

   ```bash
   cp -r <uasep-repo>/kit/uasep <your-repo>/tests/
   ```

2. Make sure `jsonschema` and `pyyaml` are installed in your test
   environment (the kit skips schema checks with a clear message when they
   are missing).

3. Run:

   ```bash
   python -m pytest tests/uasep -q
   ```

## Versioning

The schema snapshots in `uasep/schemas/` are pinned to the kit's protocol
version. When you bump `protocol_version` in your manifest, update the kit
from the matching UASEP release. The kit is versioned with the protocol
repository, not independently.

## Notes

- The kit validates **protocol artifacts only**; it does not run your
  project's tests or CI — those remain your project's own evidence.
- If your manifest fails schema validation after a protocol upgrade, read
  the UASEP changelog for migration notes (e.g. 3.4.0 → 3.5.0 renamed
  `runtime` to `uasep_runtime` and added optional `project_runtime` /
  `project` fields).
