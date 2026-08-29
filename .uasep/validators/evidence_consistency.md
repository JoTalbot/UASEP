# Evidence Consistency Checker

## Purpose
Validate that completed work has traceable evidence and that claims match recorded artifacts.

## Checks

- Evidence reference exists
- Artifact path is valid
- Verification status is explicit
- UNKNOWN is used when validation is unavailable
- Completion claims require supporting records

## States

READY
VERIFIED
UNKNOWN
BLOCKED

## Validation Flow

Claim -> Evidence -> Artifact -> Verification -> State Update

## Rules

No evidence means no verified completion.
Evidence must describe what was checked and how.