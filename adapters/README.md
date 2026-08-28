# UASEP Adapters

UASEP is runtime-free. Adapters are documentation-level capability mappings, not executable runtime components.

For the current Chat + GitHub Connector operating model, agents should use only capabilities actually exposed by the connected session.

## Capability contract

Where the environment supports them, an agent may identify capabilities such as:

- `discover_capabilities`
- `read_project`
- `read_state`
- `write_artifact`
- `execute`
- `test`
- `git`
- `handoff`

Unavailable operations MUST be reported as `UNKNOWN` or `BLOCKED`; agents must never fabricate side effects.

## Current environment

The canonical operating environment is **chat + connected GitHub tools**.

A local CLI, sandbox, autonomous executor, or separate runtime is not part of the current UASEP architecture.
