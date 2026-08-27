# UASEP Adapters

Adapters translate environment-specific tools into UASEP capabilities.

An adapter should expose, where supported:

- `discover_capabilities`
- `read_project`
- `read_state`
- `write_artifact`
- `execute`
- `test`
- `git`
- `handoff`

Adapters must report unavailable operations honestly. They must not fabricate side effects.

Planned adapters:

- `chatgpt-github`
- `local-cli`
- `sandbox`
- `aios2`
