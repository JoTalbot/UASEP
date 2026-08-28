# Skill: Self-Maintenance

UASEP agents may improve the protocol while working, but maintenance must never silently change operational contracts.

## Inspect

Look for stale instructions, contradictory rules, missing handoff data, undocumented recurring failures, and unnecessary complexity.

## Change

Prefer small documentation-first improvements. Update the relevant protocol, skill, template, state, or example together so the repository remains internally consistent.

## Protect

Do not remove useful historical evidence. Do not rewrite decisions to make history look cleaner. Record important changes in `protocol/` or `.uasep/knowledge/DECISIONS.md`.

## Verify

After maintenance, check links/paths referenced by the changed documents, inspect the diff, and confirm that the new rule is unambiguous to an agent with no chat history.

## Stop condition

Do not invent automation merely to automate the protocol. If chat + GitHub tools already provide the needed behavior, documentation is the preferred implementation.
