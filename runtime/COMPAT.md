# Runtime compatibility notes

## Canonical modules

| Concern | Canonical | Compatibility |
|---------|-----------|---------------|
| Checkpoints (journal) | `checkpoint_store.py` | `checkpoints_v2` re-exports |
| Named/atomic checkpoints | `checkpoints.py` | RecoveryManager |
| Stagnation (window) | `anti_loop.py` | — |
| Stagnation (failure streak) | `anti_loop_v2.py` | different API on purpose |
| Approval gate | `approval_gate.py` | `approval.py` older enum API |
| Executor | `executor.py` | `execution.py` result wrapper |
| Replan | `replan.py` / `replanning.py` | two TaskGraph styles; both kept |

Prefer canonical imports in new code.
