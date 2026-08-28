# Bootstrap Resolution

UASEP is runtime-free. The bootstrap process is therefore performed by the chat agent using the capabilities exposed by the connected environment.

## Resolution order

The agent must resolve the protocol from the strongest available source in this order:

1. Project-local `.uasep/` matching a compatible version.
2. Trusted UASEP source repository.
3. Protocol files already supplied through the connected GitHub environment.
4. Minimal embedded bootstrap behavior available in the chat session.

A separate UASEP runtime, local CLI, autonomous executor, or bundled runtime protocol is **not** required and is not part of the current architecture.

## Bootstrap procedure

Before starting work, the agent must:

1. Identify the repository and active branch.
2. Read the root `AGENTS.md`.
3. Resolve the applicable UASEP protocol and compatibility version.
4. Read `.uasep/state/STATUS.md`, `PROJECT_STATE.md`, and `HANDOFF.md` when present.
5. Inspect active ownership, task write sets, and recent evidence before claiming work.
6. Determine which operations are actually available through the connected environment.
7. State any unavailable capability as `UNKNOWN` or `BLOCKED` rather than inventing a side effect.

The agent must record the source actually used for protocol resolution when durable state is updated.

If the full protocol cannot be loaded, the agent may operate in degraded bootstrap mode but must not claim full UASEP compliance.

A project-local protocol may add project-specific rules but must not silently weaken core safety, truth, evidence, integrity, ownership, or handoff requirements.
