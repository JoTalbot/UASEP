from pathlib import Path

from runtime.autonomous_loop import AutonomousLoop
from runtime.compatibility import LegacyRuntime
from runtime.task_graph import TaskGraph, TaskNode


def test_legacy_runtime_is_explicit_compatibility_boundary(tmp_path: Path):
    loop = AutonomousLoop(tmp_path, "demo", TaskGraph([TaskNode("x", "X")]))
    result = LegacyRuntime(loop).run_once(lambda task: True, lambda task: [("acceptance", lambda: True)])
    assert result.status == "VERIFIED"
