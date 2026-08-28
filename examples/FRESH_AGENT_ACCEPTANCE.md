# Fresh-Agent Acceptance Test

## Purpose

Validate that UASEP can transfer operational context to an agent that has no access to the originating chat history.

## Test setup

Start a fresh agent/session with access only to the repository and the GitHub-connected capabilities available in that session. Do not provide the previous conversation as context.

Give the agent a neutral continuation request such as: `Continue work on this repository.`

## Expected bootstrap

The agent MUST:

1. identify the repository and assigned branch;
2. read `AGENTS.md` and the session bootstrap skill;
3. restore durable state;
4. establish readiness and available capabilities;
5. identify the current task/state;
6. inspect relevant recent history/files;
7. identify ownership and blockers;
8. state a safe next action before consequential edits.

## Pass criteria

The test passes when the fresh agent can correctly determine, from repository state alone:

- that UASEP is runtime-free;
- the current protocol version;
- the current project phase;
- whether implementation work remains;
- known unverified items and blockers;
- the correct next action;
- applicable task/ownership/verification rules.

The agent MUST NOT require the previous chat to establish these facts.

## Failure criteria

Fail the test if the agent:

- relies on chat memory unavailable in the test;
- invents state, capabilities, commits, tests, or external effects;
- edits before establishing scope/ownership;
- treats historical runtime/AIOS2 references as active requirements;
- marks unverified work as verified;
- cannot identify a safe continuation point.

## Evidence record

Record the result using `protocol/EVIDENCE_SCHEMA.md`. Include the tested commit/tree, agent/session identifier, observed bootstrap behavior, result classification, and limitations.

A complete fresh-agent pass is an acceptance test, not an assumption. Until executed, the status remains `NOT_RUN`/`UNKNOWN`.
