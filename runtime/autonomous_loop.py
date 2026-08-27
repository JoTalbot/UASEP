from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

from .approval_gate import ApprovalGate, ApprovalRequest
from .checkpoint_store import CheckpointStore
from .evidence_store import Evidence, EvidenceStore
from .replanning import Replanner
from .retry_policy import RetryPolicy
from .state import StateStore
from .task_graph import TaskGraph, TaskNode
from .verification import VerificationEngine


@dataclass(frozen=True, slots=True)
class CycleResult:
    task_id: str | None
    status: str
    iterations: int
    reason: str = ""


class AutonomousLoop:
    """Bounded, resumable engineering cycle with verification and recovery hooks."""

    def __init__(self, root: Path, project_id: str, graph: TaskGraph) -> None:
        self.root = root
        self.project_id = project_id
        self.graph = graph
        self.state_store = StateStore(root)
        self.evidence = EvidenceStore(root / ".uasep" / "evidence" / "runtime.json")
        self.checkpoints = CheckpointStore(root / ".uasep" / "checkpoints" / "journal.json")
        self.verifier = VerificationEngine()
        self.retry_policy = RetryPolicy()
        self.replanner = Replanner()
        self.approval_gate = ApprovalGate()

    def run_once(self, execute: Callable[[TaskNode], bool], checks: Callable[[TaskNode], Iterable[tuple[str, Callable[[], bool]]]], strategy: str = "default", approval: Callable[[ApprovalRequest], bool] | None = None) -> CycleResult:
        state = self.state_store.load(self.project_id)
        ready = self.graph.ready()
        if not ready:
            state.phase = "complete" if not self.graph.tasks or len(self.graph.completed()) == len(self.graph.tasks) else "blocked"
            self.state_store.save(state)
            return CycleResult(None, state.phase.upper(), state.iteration)
        task = ready[0]
        state.current_task = task.id
        state.phase = "executing"
        state.iteration += 1
        self.state_store.save(state)
        self.checkpoints.save(task.id, "executing")
        request = ApprovalRequest(f"execute:{task.id}", f"execute task {task.id}", destructive=False)
        if not self.approval_gate.check(request) or (approval is not None and not approval(request)):
            state.phase = "blocked"
            self.state_store.save(state)
            return CycleResult(task.id, "BLOCKED", state.iteration, "approval required")
        if not execute(task):
            decision = self.retry_policy.decide(task.id, state.iteration, strategy)
            state.phase = "blocked"
            self.evidence.record(Evidence("execution", task.id, "FAILED", decision.reason))
            self.state_store.save(state)
            self.checkpoints.save(task.id, "failed")
            return CycleResult(task.id, "FAILED", state.iteration, decision.reason)
        verification = self.verifier.verify(checks(task))
        self.evidence.record(Evidence("verification", task.id, verification.status, "; ".join(verification.details)))
        if verification.status != "VERIFIED":
            decision = self.retry_policy.decide(task.id, state.iteration, strategy)
            replan = self.replanner.choose(self.graph, task.id)
            state.phase = "blocked"
            self.state_store.save(state)
            self.checkpoints.save(task.id, "verification_failed")
            return CycleResult(task.id, "FAILED", state.iteration, f"{decision.reason}; {replan.reason}")
        self.graph.mark_done(task.id)
        state.completed_tasks.add(task.id)
        state.current_task = None
        state.phase = "complete" if not self.graph.ready() else "active"
        self.state_store.save(state)
        self.checkpoints.save(task.id, "verified")
        self.evidence.record(Evidence("completion", task.id, "VERIFIED", "acceptance checks passed"))
        return CycleResult(task.id, "VERIFIED", state.iteration)
