# UASEP Runtime Discovery Contract

This contract defines how a host locates and activates UASEP before autonomous development begins.

## Discovery order

1. Resolve the project root from the host's current working context or explicit project path.
2. Detect an existing `.uasep/` directory and preserve its state.
3. Locate the UASEP protocol/runtime from the local project, an installed package, or a host-provided repository source.
4. Determine which host capabilities are actually available. Never infer unavailable capabilities.
5. Select the canonical UASEP runtime boundary exposed by the host.
6. Bootstrap a new project when no valid state exists, otherwise resume the existing state.

## Host neutrality

The discovery contract does not assume GitHub, a local CLI, a sandbox, or any particular operating system. The host is responsible for exposing capabilities through the UASEP adapter boundary.

## Failure behavior

If UASEP cannot be located, the host cannot establish a writable project root, or required capabilities are unavailable, execution MUST stop with an explicit blocker. The agent MUST NOT silently substitute undocumented behavior.

## Persistence

When `.uasep/` exists, its state, evidence, checkpoints, planning data, and manifest are authoritative inputs to resume unless integrity validation rejects them.

## Security

Privileged, destructive, external, or irreversible operations remain subject to the host's approval and safety boundaries. Discovery MUST NOT grant capabilities that the host did not explicitly expose.
