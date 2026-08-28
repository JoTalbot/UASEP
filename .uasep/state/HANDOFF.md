# Handoff — branch `new`

Independent of `main`.

## Canonical

- Supervisor + Store + TaskGraph + models
- `adapters/local_cli.py` wired from CLI `run`/`resume`
- Validator runs only unified tests

## Removed (partial)

anti_loop*, approval.py, checkpoints*, checkpoint_store, evidence_store, aios2_adapter, execution, executor, …

## Still optional cleanup

Leftover files under `runtime/` and legacy tests may remain until deleted; they are outside the validation path.
