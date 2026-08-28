# Protocol Drift Detection

Drift occurs when repository instructions, durable state, skills, examples, or normative protocol rules disagree about how agents should operate.

## Detection checklist

During periodic maintenance or before a major batch, inspect for:

- references to retired runtime components;
- obsolete AIOS2 assumptions;
- duplicate or competing state-of-truth files;
- skills that contradict `protocol/CONFORMANCE.md`;
- examples that claim capabilities unavailable in the target environment;
- stale task statuses or ownership claims;
- instructions that require chat history rather than repository state;
- completion claims without evidence.

## Resolution order

1. `protocol/` defines normative requirements.
2. `AGENTS.md` defines the mandatory project agent contract.
3. `skills/` provide reusable procedures consistent with the protocol.
4. `.uasep/state/` records current operational facts.
5. `examples/` illustrate compliant behavior and must not weaken normative rules.
6. Project-specific instructions may specialize behavior only where compatible with the core protocol.

If two sources conflict, do not silently choose one. Record the conflict, determine the authoritative source, correct the stale artifact, and record the decision/evidence.

## Safe audit

Prefer read-only inspection first. Make narrow changes with explicit evidence. Do not rewrite historical commits solely to remove wording from history; historical references may remain as provenance. The requirement is that the active tree and current operating instructions are internally consistent.

## Completion

A drift audit is complete when known active-tree contradictions are resolved, stale operational state is retired, and remaining unknowns are explicitly recorded rather than presented as verified.
