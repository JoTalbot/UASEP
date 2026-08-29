# C90.2 Ecosystem State Intelligence

## State model
Represent external systems through normalized observations with source, timestamp, confidence, freshness, and provenance.

## Processing
1. Collect permitted observations.
2. Validate and normalize data.
3. Detect stale or conflicting observations.
4. Correlate related state changes.
5. Calculate bounded confidence.
6. Publish an auditable ecosystem snapshot.

## Reliability
Conflicting sources must not be silently merged. Low-confidence or stale observations are explicitly marked and must not trigger unrestricted side effects.