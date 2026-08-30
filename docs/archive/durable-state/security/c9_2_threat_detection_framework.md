# C9.2 Threat Detection Framework

## Purpose
Framework for identifying, classifying and responding to security threats.

## Capabilities

- threat signal collection
- anomaly detection
- threat classification
- severity assessment
- evidence correlation
- response preparation

## Pipeline

Threat Signal
↓
Detection Analysis
↓
Classification
↓
Risk Evaluation
↓
Response Decision
↓
Audit Record

## Threat States

- OBSERVED
- ANALYZING
- CONFIRMED
- MITIGATING
- RESOLVED
- UNKNOWN

## Rules

- no automatic trust of unverified signals
- all decisions require traceability
- confirmed incidents must produce evidence
