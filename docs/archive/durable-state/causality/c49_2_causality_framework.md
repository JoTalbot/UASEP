# C49.2 Autonomous Causality Framework

## Purpose
Provide deterministic, auditable infrastructure for constructing and evaluating causal analyses across UASEP events, states, dependencies, interventions and outcomes while preserving uncertainty, provenance and governance boundaries.

## Capabilities
- versioned causal graph storage
- temporal and dependency relationships
- causal hypothesis registry
- intervention and counterfactual experiment records
- confounder and alternative-hypothesis tracking
- evidence/provenance references
- reproducible analysis execution
- causal result classification
- access control and retention
- escalation and approval hooks

## Causal analysis pipeline
```text
Causal Question
  -> Scope / Preconditions
  -> Event + State Timeline
  -> Dependency Mapping
  -> Candidate Causal Graph
  -> Alternatives / Confounders
  -> Intervention / Counterfactual Analysis
  -> Evidence Evaluation
  -> Supported / Unsupported / Unknown
  -> Provenance + Verification Record
  -> Governed Explanation
```

## Causal analysis record
Each material analysis should declare:
- analysis identifier and version
- target cause/effect variables
- scope and assumptions
- temporal ordering
- candidate graph and dependencies
- alternative hypotheses/confounders
- interventions or counterfactual tests
- supporting and contradictory evidence
- evidence provenance
- confidence and uncertainty
- result classification

## Reproducibility
Material causal conclusions retain the graph, assumptions, evidence references, analysis/validator versions and relevant execution metadata needed for independent reconstruction.

## Result semantics
- `SUPPORTED`: evidence provides sufficient support under declared assumptions.
- `UNSUPPORTED`: available evidence contradicts or fails the required causal criteria.
- `UNKNOWN`: evidence, intervention, or identification conditions are insufficient.

`UNKNOWN` is not equivalent to `SUPPORTED`.

## Safety invariants
1. Correlation cannot be promoted to causation without causal evidence.
2. Temporal precedence alone is insufficient proof.
3. Alternative explanations remain visible for material conclusions.
4. Source evidence is immutable or provenance-preserving.
5. Causal analysis cannot bypass authorization or grant execution authority.
6. High-impact causal conclusions require appropriate verification or escalation.
7. Experiments and interventions run within explicitly scoped capabilities and isolation.

## Integration
- C49.1 Causality Intelligence Engine
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
The framework is ready when material causal analyses can be versioned, reproduced, evaluated against explicit criteria, linked to evidence and provenance, and classified with explicit uncertainty without confusing correlation with causation or granting execution authority.
