# Runtime compatibility notes

## Dual modules

- `anti_loop.py` — windowed stagnation detector (canonical for tests).
- `anti_loop_v2.py` — failure-streak API; prefer canonical until consolidated.
- `checkpoint_store.py` / `checkpoints.py` / `checkpoints_v2.py` — prefer `checkpoint_store` for new code.

Consolidation is deferred; do not break import paths used by tests.
