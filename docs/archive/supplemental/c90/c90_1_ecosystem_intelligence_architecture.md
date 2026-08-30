# C90.1 Autonomous Ecosystem Intelligence Architecture

## Purpose
Coordinate observations and capabilities across trusted external integrations without bypassing governance controls.

## Core loop
Observe -> normalize -> correlate -> evaluate -> plan -> authorize -> act -> measure -> learn.

## Design rules
- External state is untrusted until validated.
- Intelligence cannot grant itself permissions.
- Side effects require explicit authorization and policy evaluation.
- Decisions are observable and auditable.
- Failure domains remain isolated.
- Resource use is bounded.

## Intelligence domains
- ecosystem state aggregation
- dependency awareness
- capability discovery
- integration health analysis
- impact assessment
- bounded optimization

## Non-goals
No unrestricted autonomy, privilege escalation, policy bypass, or opaque external actions.