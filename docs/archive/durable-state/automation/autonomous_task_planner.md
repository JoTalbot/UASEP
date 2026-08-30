# C4.1 Autonomous Task Planner

## Purpose
Define a controlled planning layer for autonomous operations.

## Checks

- task decomposition
- dependency discovery
- priority evaluation
- ownership assignment
- verification planning

## Safety Rules

- no execution without task contract
- no completion without evidence
- blocked states remain explicit
- planning does not override protocol constraints

## Flow

Request
 -> Task Analysis
 -> Plan Generation
 -> Risk Check
 -> Execution Contract
 -> Verification
