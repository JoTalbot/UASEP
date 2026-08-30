# UASEP Template Applier

## Purpose

Applies approved automation templates to target repositories.

## Flow

Audit result

```
Repository Audit
        ↓
Template Selection
        ↓
Workflow Generation
        ↓
Validation
        ↓
Evidence Update
```

## Supported templates

- CI
- Release
- Security
- Maintenance

## Rules

- Never overwrite without validation
- Preserve evidence
- Verify generated workflows
- Keep repository state synchronized
