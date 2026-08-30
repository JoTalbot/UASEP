# C6.2 Automated Refactoring Proposals

## Purpose
Define a controlled process for proposing structural and code improvements.

## Principles
- No refactoring without impact analysis.
- Every proposal requires evidence.
- Changes must preserve architecture contracts.

## Pipeline

Request
→ Code Analysis
→ Refactoring Proposal
→ Impact Review
→ Validation
→ Approval
→ Implementation

## Checks

- dependency analysis
- regression risk assessment
- compatibility verification
- test requirements
- rollback planning

## Status Model

PROPOSED
REVIEWING
APPROVED
REJECTED
UNKNOWN
