# UASEP Versioning and Migration

Version: 3.1.2 contract

## Version scheme

`MAJOR.MINOR.PATCH`

- **MAJOR** — breaking change to core lifecycle, state schema, or completion invariant.
- **MINOR** — new capabilities, optional fields, new protocol docs; backward-compatible resume.
- **PATCH** — fixes, hardening, evidence, non-breaking runtime behavior.

`VERSION` file and `pyproject.toml` must match.

## State compatibility

1. Load must tolerate missing optional fields (default them).
2. New required fields need a migration step and a MINOR or MAJOR bump.
3. Never silently discard incompatible `.uasep` state; record a blocker and offer migration.

## Migration rules

1. Detect `protocol_version` (or absence) in `.uasep/state.json` / manifest.
2. Apply ordered migrations up to the runtime version.
3. Write migrated state with the new version; keep evidence of migration.
4. If migration is unsafe or ambiguous, stop with an explicit blocker.

## Example migrations

| From | To | Action |
|------|-----|--------|
| (none) / 3.1.0 | 3.1.1 | No state change; cycle-budget contract is runtime-only |
| 3.1.1 | 3.1.2 | Ensure `task_failures` defaults to `{}` if missing |

## Agent duty

On resume: if stored version &lt; runtime version, run migrations before planning.
On upgrade of protocol docs: update `VERSION`, CHANGELOG, and this table.
