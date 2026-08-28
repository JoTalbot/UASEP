# Adapters

Host adapters map abstract UASEP capabilities to concrete environments.

## Current
- **HostAdapter** (`runtime/host_adapter.py`) — generic capability registry.
- **AIOS2** (`runtime/aios2_adapter.py`) — stub contract for AIOS2 runtime.

## Planned
- Richer AIOS2 end-to-end (ADOPT-001).
- Local CLI beyond `runtime.cli` (ADOPT-003).
- ChatGPT/GitHub operational path documented in `examples/chatgpt-github-workflow.md`.

## Contract
Adapters must expose discoverable capabilities with `available`, `approval_required`, and `source` metadata. Execution only through declared capabilities.
