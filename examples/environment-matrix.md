# Environment Matrix

UASEP is currently designed for use inside AI chats with connected GitHub tools. The repository is the durable memory and coordination layer; the chat agent is the execution environment.

| Environment | Typical capabilities | Degraded behavior |
|---|---|---|
| Chat + GitHub Connector | repository read/write, GitHub APIs, available web/tools | no local shell; use repository inspection and available checks |

The matrix is intentionally limited to the supported operating model. UASEP does not require a local CLI, sandbox, IDE agent, autonomous executor, or separate runtime.

Capability discovery is authoritative for the current chat session. Unsupported operations MUST be reported as `UNKNOWN` or `BLOCKED`; agents must never fabricate side effects.
