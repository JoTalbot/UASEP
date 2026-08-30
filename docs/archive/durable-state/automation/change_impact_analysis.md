# C4.3 Change Impact Analysis

## Purpose
Analyze possible system impact before applying changes.

## Checks

- affected components discovery
- dependency analysis
- contract compatibility review
- regression risk identification
- verification requirements generation

## Flow

Request
  -> Impact Analysis
  -> Dependency Map
  -> Risk Assessment
  -> Verification Plan
  -> Change Decision

## Status Model

- SAFE
- REVIEW_REQUIRED
- BLOCKED
- UNKNOWN

## Rule

No change is considered isolated until affected boundaries are identified.
