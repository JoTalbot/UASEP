# UASEP Task Executor

## Purpose
Controlled execution layer for automation tasks.

Flow:

Request
  -> Action Queue
  -> Task Executor
  -> Verification
  -> Evidence Update

Responsibilities:

- execute approved automation jobs
- track execution state
- report results
- integrate with verification engine
