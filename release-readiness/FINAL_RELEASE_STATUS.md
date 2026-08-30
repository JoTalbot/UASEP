# UASEP Final Release Status

## Pipeline Status

- Canonical conformance suite: READY (54 repository-native pytest checks)
- Release gate: READY (manual dispatch; runs the full suite)
- Automated tag/release flow: READY (tag derived from `VERSION`)
- Post-release verification: READY (published-tag integrity check)

## Release Flow

1. A commit lands on `main` and the canonical conformance suite passes.
2. A maintainer dispatches **UASEP Release Gate** on the commit to release.
3. On gate success, **UASEP Automated Release** tags the verified commit with `v$(VERSION)`, creates the GitHub release, and verifies the tag and release target in-workflow (events caused by `GITHUB_TOKEN` do not trigger other workflows, so the automated path cannot rely on the `release` event).
4. **UASEP Release Verification** additionally confirms tag integrity for releases published by other means (manual PAT/API publishes).

## Release Rule

Releases are deliberate: the gate is manual, tags follow the `VERSION` file,
and a release is only considered ready when every automated gate passes on the
exact commit being released. Releasing the same version twice fails; bump
`VERSION` first.
