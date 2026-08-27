from pathlib import Path

from runtime.acceptance import AcceptanceEngine
from runtime.approval import ApprovalGate
from runtime.replan import Replanner
from runtime.task_graph import TaskGraph, TaskNode


def test_acceptance_requires_all_criteria():
    engine = AcceptanceEngine()
    results = engine.evaluate([("one", lambda: True), ("two", lambda: False)])
    assert not engine.accepted(results)


def test_replanner_switches_to_independent_task():
    graph = TaskGraph([TaskNode("failed", "Failed"), TaskNode("other", "Other", priority=10)])
    result = Replanner().choose(graph, "failed")
    assert result.action == "switch_task"
    assert result.reason.endswith("other")


def test_approval_gate_blocks_unapproved_action():
    request = ApprovalGate().require("delete", "destructive operation")
    assert not ApprovalGate.can_execute(request)
