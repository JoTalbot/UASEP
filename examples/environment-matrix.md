# Environment Matrix

The same bootstrap adapts to different environments.

| Environment | Typical capabilities | Degraded behavior |
|---|---|---|
| ChatGPT + GitHub | repository read/write, GitHub APIs, web when available | no shell execution; use repository inspection and available checks |
| Local CLI | filesystem, shell, git, build, tests | use local runtime directly |
| Temporary sandbox | filesystem, shell, isolated compute | persist handoff before expiry |
| IDE agent | workspace, editor, tests | use IDE-native capabilities |
| AIOS2 runtime | supervisor, task graph, agents, tools | use runtime orchestration |

The matrix is illustrative. Runtime discovery is authoritative.
