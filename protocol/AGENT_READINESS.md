# UASEP Agent Readiness

Before consequential work, the agent should establish a compact readiness state.

## Readiness checklist

```text
UASEP READY
Repository: <owner/name>
Branch: <exact branch>
Protocol: <version>
State: <current phase>
Active tasks: <count>
Ownership conflicts: <count>
Blockers: <count>
Capabilities: <verified capabilities>
Runtime: NONE
```

## Requirements

`READY` means the agent has actually inspected the repository state, applicable instructions, ownership, and available capabilities. It does not mean every requested operation is guaranteed to succeed.

If a required prerequisite cannot be established, use `BLOCKED` or `UNKNOWN` and record the reason.

The readiness summary is a working snapshot, not a substitute for durable state. When consequential work changes state, update the appropriate durable artifact.
