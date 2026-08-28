from __future__ import annotations

import os
import time
from contextlib import contextmanager
from pathlib import Path


class ProjectLockError(RuntimeError):
    pass


@contextmanager
def project_lock(root: str | Path, *, timeout: float = 10.0):
    """Exclusive project lock using atomic lock-file creation."""
    lock_path = Path(root) / ".uasep" / "runtime.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + timeout
    fd: int | None = None
    while fd is None:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode("ascii"))
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise ProjectLockError(f"timed out waiting for {lock_path}")
            time.sleep(0.05)
    try:
        yield
    finally:
        os.close(fd)
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass
