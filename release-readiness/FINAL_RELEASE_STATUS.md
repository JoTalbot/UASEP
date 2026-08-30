# UASEP Final Release Status

## Pipeline Status

- Canonical conformance suite: READY (54 repository-native pytest checks)
- Release gate: READY (manual dispatch; runs the full suite)
- Automated tag/release flow: READY (tag derived from `VERSION`)
- Post-release verification: READY (published-tag integrity check)

## Release Flow

1. A commit lands on `main` and the canonical conformance suite passes.
2. A maintainer dispatches **UASEP Release Gate** on the commit to release.
3. On gate success, **UASEP Automated Release** tags the verified commit with `v$(VERSION)` and creates the GitHub release.
4. **UASEP Release Verification** confirms the published tag integrity.

## Release Rule

Releases are deliberate: the gate is manual, tags follow the `VERSION` file,
and a release is only considered ready when every automated gate passes on the
exact commit being released. Releasing the same version twice fails; bump
`VERSION` first.
