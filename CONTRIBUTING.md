# Contributing to UASEP

## Setup

```bash
python -m pip install pytest
python -m pytest -q
```

## CLI

```bash
python -m runtime.cli bootstrap
python -m runtime.cli check
python -m runtime.cli status
python -m runtime.cli plan
python -m runtime.cli run --task-id demo
```

## Rules

- Prefer small PRs with tests
- Do not invent CI results
- Update `.uasep` state/handoff when completing work
- Keep VERSION and pyproject version aligned
