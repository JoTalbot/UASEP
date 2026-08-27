from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .host_adapter import HostAdapter
from .models import Task


@dataclass(slots=True)
class HostExecutor:
    """Translate a task into a host capability request without assuming the host."""

    host: HostAdapter
    capability: str = "project.execute"
    handler: Callable[[Task], bool] | None = None

    def __call__(self, task: Task) -> bool:
        if self.handler is not None:
            return bool(self.handler(task))
        return bool(self.host.request(self.capability, task))
