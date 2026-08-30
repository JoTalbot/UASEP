# UASEP Notification Connector

Event notification integration for automation workflows.

## Responsibilities

- publish automation status events
- deliver failure and recovery alerts
- summarize executions
- preserve notification evidence

## Safety

Notifications must not contain secrets or credentials. Delivery failures are recorded without blocking core state persistence unless policy explicitly requires delivery confirmation.
