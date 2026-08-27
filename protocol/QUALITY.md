# Quality Protocol

Quality is evidence-based and proportional to risk.

## Gates

- correctness
- tests
- build/package
- security
- compatibility
- documentation
- integration

Not every project requires every gate, but skipped gates must be explicit.

## Definition of Done

A task is DONE only when:

1. acceptance criteria are satisfied;
2. implementation is integrated or deliberately isolated;
3. appropriate tests/checks have run;
4. important risks are reviewed;
5. evidence is recorded;
6. project state is updated.

## Change impact

Before broad changes, inspect dependencies, interfaces, affected tests, documentation, and migration needs.

## Architecture drift

Periodically compare intended architecture with actual architecture. Create refactoring or documentation tasks when drift becomes material.
