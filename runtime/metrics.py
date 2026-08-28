from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Metrics:
    """Lightweight process metrics for self-maintenance signals."""

    tasks_started: int = 0
    tasks_verified: int = 0
    tasks_failed: int = 0
    retries: int = 0
    cycles: int = 0
    notes: list[str] = field(default_factory=list)

    def record_start(self) -> None:
        self.tasks_started += 1

    def record_verified(self) -> None:
        self.tasks_verified += 1

    def record_failed(self, retry: bool = False) -> None:
        self.tasks_failed += 1
        if retry:
            self.retries += 1

    def record_cycle(self) -> None:
        self.cycles += 1

    def snapshot(self) -> dict[str, int]:
        return {
            "tasks_started": self.tasks_started,
            "tasks_verified": self.tasks_verified,
            "tasks_failed": self.tasks_failed,
            "retries": self.retries,
            "cycles": self.cycles,
        }
