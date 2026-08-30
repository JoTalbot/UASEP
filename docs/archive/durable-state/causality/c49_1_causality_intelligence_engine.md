# C49.1 Autonomous Causality Intelligence Engine

## Purpose
Provide a governed intelligence layer for analyzing candidate causal relationships, reconstructing root-cause hypotheses and distinguishing correlation from causally supported conclusions across UASEP events, states, decisions and outcomes.

## Capabilities
- causal graph construction
- temporal ordering analysis
- dependency and intervention analysis
- root-cause hypothesis generation
- competing-hypothesis analysis
- confounder and common-cause detection
- counterfactual reasoning
- evidence sufficiency assessment
- confidence and uncertainty estimation
- causal explanation and provenance
- incident root-cause reconstruction

## Causal flow
```text
Events / States / Outcomes
    -> Temporal + Dependency Mapping
    -> Candidate Causal Graph
    -> Confounder / Alternative Analysis
    -> Intervention / Counterfactual Tests
    -> Evidence Assessment
    -> Root-Cause Hypotheses
    -> Confidence + Uncertainty
    -> Governed Causal Conclusion
    -> Provenance / Verification Record
```

## Causal subjects
- operational incidents
- security events
- configuration changes
- deployment/recovery operations
- agent/model decisions
- policy changes
- dependency failures
- resource saturation
- simulation and validation outcomes

## Evidence model
Material causal claims should retain:
- cause/effect candidates
- temporal ordering
- supporting observations
- intervention or experimental evidence where available
- alternative hypotheses
- confounders considered
- confidence and uncertainty
- provenance references
- validation status

## Causal semantics
Correlation is not causation. Temporal precedence alone is not proof of causality. A causal conclusion must state its evidence strength and uncertainty and distinguish observed relationships from experimentally or otherwise strongly supported causal effects.

## Safety invariants
1. Correlation cannot silently become a causal fact.
2. Alternative explanations remain visible for material conclusions.
3. Missing evidence lowers confidence and remains explicit.
4. Causal analysis cannot modify source evidence.
5. Causal conclusions do not grant execution authority.
6. High-impact root-cause claims require appropriate verification or escalation.
7. Provenance and reproducibility are retained for material causal analyses.

## States
`UNANALYZED -> MAPPING -> HYPOTHESIZING -> TESTING -> EVALUATING -> SUPPORTED / UNSUPPORTED / UNKNOWN -> RECORDED`

Failure paths:
- `MAPPING -> INCOMPLETE`
- `TESTING -> INSUFFICIENT_EVIDENCE`
- `EVALUATING -> CONFLICTING`
- `EVALUATING -> ESCALATED`

## Integration
- C48 Provenance & Integrity
- C47 Verification
- C46 Observability
- C45 Trust and Compliance
- C44 Security
- C43 Resilience
- C42 Simulation
- C41 Orchestration
- C40 Learning
- C39 Governance
- C38 Action
- C37 Decision

## Completion criterion
The causality intelligence layer is ready when material UASEP incidents, changes and outcomes can be analyzed through temporal, dependency, alternative and intervention evidence, with causal claims explicitly separated from correlation and recorded with provenance and uncertainty.
