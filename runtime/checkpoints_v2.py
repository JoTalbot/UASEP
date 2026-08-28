"""Compatibility alias — prefer runtime.checkpoint_store."""
from __future__ import annotations

from .checkpoint_store import Checkpoint, CheckpointStore

__all__ = ["Checkpoint", "CheckpointStore"]
