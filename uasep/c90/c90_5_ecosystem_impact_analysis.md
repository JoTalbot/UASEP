# C90.5 Ecosystem Impact Analysis

## Purpose
Estimate the consequences of proposed actions across the connected ecosystem before execution.

## Impact dimensions
- availability
- integrity
- confidentiality boundaries
- resource consumption
- dependency health
- policy and compliance exposure
- downstream side effects

## Decision flow
1. Build the affected dependency graph.
2. Identify direct and indirect effects.
3. Classify severity and confidence.
4. Check authorization and governance policies.
5. Require approval when risk exceeds the permitted automation threshold.
6. Record the analysis and final decision.

## Safety
Unknown impact must be treated as uncertainty, not as permission. High-risk actions require explicit authorization.