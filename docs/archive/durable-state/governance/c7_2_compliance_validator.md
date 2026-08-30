# C7.2 Compliance Validator

## Purpose

Validate that system state, agents, artifacts and decisions comply with defined governance requirements.

## Capabilities

- Policy compliance checks
- Artifact requirement validation
- Evidence availability verification
- State consistency checks
- Detection of governance violations
- Compliance reporting

## Pipeline

Request
  ↓
Compliance Analysis
  ↓
Requirement Mapping
  ↓
Validation
  ↓
Compliance Report
  ↓
Governance Update

## Statuses

- COMPLIANT
- REVIEW_REQUIRED
- NON_COMPLIANT
- UNKNOWN

## Rules

- No compliance claim without evidence
- Unknown state must remain UNKNOWN
- Violations require traceable records
- Changes require validation before acceptance
