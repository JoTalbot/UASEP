# C43.1 Autonomous Resilience Intelligence Engine

## Purpose
Provide a governed intelligence layer for detecting, assessing and coordinating responses to faults, degradation and recovery conditions across UASEP without weakening safety, authorization or observability.

## Capabilities
- fault and anomaly detection
- health and dependency analysis
- failure impact assessment
- resilience risk scoring
- degradation-mode classification
- recovery strategy selection
- failure containment planning
- recovery readiness assessment
- resilience recommendations
- post-incident learning feedback

## Resilience flow
```text
System Health / Events
    -> Fault Detection
    -> Context + Dependency Analysis
    -> Impact Assessment
    -> Resilience Risk Evaluation
    -> Recovery Strategy Selection
    -> Governance Validation
    -> Containment / Recovery Plan
    -> Outcome Assessment
    -> Learning Feedback
```

## Failure classes
- transient failure
- persistent failure
- dependency failure
- resource exhaustion
- degraded service
- data integrity concern
- configuration regression
- environmental fault
- cascading failure

## Recovery priorities
1. preserve safety and data integrity
2. contain propagation
3. maintain critical capabilities
4. restore service
5. validate recovered state
6. record evidence and improve future resilience

## Safety invariants
- resilience actions cannot bypass authorization or governance
- containment cannot silently disable critical safety controls
- recovery strategies must respect capability boundaries
- uncertain fault diagnosis must remain explicitly uncertain
- destructive or irreversible recovery requires appropriate approval
- recovery outcomes and failures remain auditable

## States
`OBSERVED -> DETECTED -> ASSESSING -> PLANNING -> VALIDATING -> CONTAINING -> RECOVERING -> VERIFYING -> RESTORED`

Failure paths:
- `ASSESSING -> ESCALATED`
- `VALIDATING -> BLOCKED`
- `RECOVERING -> FAILED`
- `VERIFYING -> DEGRADED`

## Integration
Coordinates with C42 Simulation, C41 Orchestration, C40 Learning, C39 Governance, C38 Action, C37 Decision and lower domain layers. It recommends and coordinates resilience behavior while domain layers retain authority over their own state and policies.
