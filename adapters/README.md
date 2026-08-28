# UASEP Adapters (branch `new`)

Adapters translate host tools into UASEP capabilities.

## local_cli (implemented)

`adapters/local_cli.py` — `LocalCliAdapter`

- `discover()` — via `runtime.discovery`
- `execute(task)` — conventions in `task.notes`
- `checks_for(task)` — conventions in `acceptance_criteria`

Wire into Supervisor:

```python
from adapters.local_cli import LocalCliAdapter
from runtime.supervisor import Supervisor

host = LocalCliAdapter(".")
sup = Supervisor(".", execute=host.execute, checks=host.checks_for)
sup.run_until_idle(project_id)
```

## Planned (not required for core)

- chatgpt-github
- sandbox
- aios2
