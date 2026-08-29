# C5.2 Agent Capability Registry

## Purpose
Define a registry describing agent abilities, responsibilities and execution boundaries.

## Capability Model

Each agent record contains:

- agent_id
- role
- capabilities
- supported tasks
- limitations
- verification requirements
- ownership scope

## Validation

Required checks:

- capability declaration exists
- ownership is defined
- task matches capability
- evidence requirements are known
- conflicts are reported

## States

READY
ACTIVE
LIMITED
BLOCKED
UNKNOWN

## Flow

Task Request
→ Capability Discovery
→ Agent Selection
→ Execution Contract
→ Verification
→ Registry Update
