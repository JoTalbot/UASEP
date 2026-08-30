# UASEP Runtime Health Monitor

## Purpose

Runtime component for monitoring execution health.

## Flow

Task Runtime
    ↓
Health Monitor
    ↓
State Update
    ↓
Self-Healing Engine
    ↓
Evidence Record

## Responsibilities

- detect failed or stalled tasks
- report runtime state
- trigger recovery analysis
- preserve execution evidence
