# Capability Discovery and Adaptation

An agent must discover what the current environment actually permits before relying on a capability.

## Capability classes

- filesystem: read, write, rename, delete
- shell: command execution, process control
- git: status, diff, branch, commit, merge, push
- github: repository, issue, pull request, actions, releases
- network: web, HTTP/API
- build: compile/package
- test: unit/integration/system tests
- containers: build/run/inspect
- browser: navigation and interaction
- database: inspect/migrate/query
- scheduling: delayed or recurring execution
- multi_agent: spawn/delegate/coordinate agents
- persistent_memory: durable memory outside chat history

## Capability record

Each capability should be represented as available, unavailable, restricted, or unknown, with optional evidence and limitations.

## Adaptation rules

- Never assume a capability exists.
- Never simulate a side effect as if it happened.
- If a capability is unavailable, choose the safest useful alternative.
- Static analysis may substitute for execution only when clearly labeled as such.
- A missing capability may lower the achievable autonomy level, but must not erase project state.
- Environment-specific adapters belong outside the core protocol.
