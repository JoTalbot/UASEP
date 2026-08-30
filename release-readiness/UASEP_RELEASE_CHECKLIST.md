# UASEP Release Readiness Checklist

## Automated gates

- [ ] Repository audit passes
- [ ] Conformance tests pass
- [ ] Production-hardening checks pass
- [ ] No credentials or token material is committed
- [ ] Required workflow permissions are explicit
- [ ] Release prerequisites are verified
- [ ] Release metadata is generated from the verified commit
- [ ] Evidence is persisted for material operations
- [ ] Failed verification blocks release completion

## Release rule

A release is considered ready only when all mandatory automated gates pass on the exact commit being released. Manual bypasses must not be represented as successful verification.

## Tagging

Tags should be created only after the release gate succeeds and should point to the exact verified commit. Release automation must be idempotent and must not silently replace an existing immutable release tag.

## Secrets

GitHub Actions secrets or environment-provided credentials must be used for authentication. Secret names must not rely on reserved `GITHUB_*` names.
