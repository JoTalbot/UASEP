# DECISION-0001 — Runtime-free architecture

## Context
UASEP is designed as a durable coordination layer for AI agents working through repository artifacts.

## Decision
Keep the core protocol repository-native. Do not require a daemon, CLI runtime, scheduler, or database service.

## Alternatives
- Mandatory runtime service.
- Central orchestration server.

## Evidence
- AGENTS.md contract.
- Protocol and conformance checks.

## Impact
Agents remain replaceable and state remains inspectable through repository artifacts.

## Status
Accepted
