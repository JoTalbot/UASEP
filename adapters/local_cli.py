"""Local CLI host adapter — honest capability discovery + execute/check conventions."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Callable

from runtime.discovery import discover_capabilities
from runtime.models import Capability, Task


class LocalCliAdapter:
    """Maps task notes / acceptance_criteria to local filesystem and optional shell."""

    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()

    def discover(self) -> list[Capability]:
        return discover_capabilities(self.root)

    def execute(self, task: Task) -> bool:
        """Execute conventions from task.notes (optional).

        Supported notes:
        - ``touch:relative/path`` — create empty file
        - ``write:relative/path<<content`` — write text
        - ``cmd:shell command`` — run if shell capability present
        - empty notes — success (planning/documentation tasks)
        """
        note = (task.notes or "").strip()
        if not note:
            return True
        if note.startswith("touch:"):
            path = self.root / note[len("touch:") :].strip()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            return True
        if note.startswith("write:"):
            rest = note[len("write:") :]
            if "<<" not in rest:
                return False
            rel, content = rest.split("<<", 1)
            path = self.root / rel.strip()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            return True
        if note.startswith("cmd:"):
            if shutil.which("python") is None and not os.access(self.root, os.X_OK):
                return False
            cmd = note[len("cmd:") :].strip()
            completed = subprocess.run(
                cmd,
                shell=True,
                cwd=self.root,
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
            return completed.returncode == 0
        # Unknown convention: do not invent success
        return False

    def checks_for(self, task: Task) -> list[tuple[str, Callable[[], bool]]]:
        """Build acceptance callables from criteria strings.

        Conventions:
        - ``file_exists:path``
        - ``file_contains:path::substring``
        - ``cmd:shell`` — exit code 0
        - other strings — treated as documentation-only (pass)
        """
        out: list[tuple[str, Callable[[], bool]]] = []
        criteria = list(task.acceptance_criteria) or ["noop"]
        for raw in criteria:
            name = raw

            if raw.startswith("file_exists:"):
                rel = raw[len("file_exists:") :].strip()

                def _exists(p: Path = self.root / rel) -> bool:
                    return p.is_file() or p.is_dir()

                out.append((name, _exists))
            elif raw.startswith("file_contains:"):
                body = raw[len("file_contains:") :]
                if "::" not in body:
                    out.append((name, lambda: False))
                    continue
                rel, needle = body.split("::", 1)
                path = self.root / rel.strip()

                def _contains(p: Path = path, n: str = needle) -> bool:
                    if not p.is_file():
                        return False
                    return n in p.read_text(encoding="utf-8")

                out.append((name, _contains))
            elif raw.startswith("cmd:"):
                cmd = raw[len("cmd:") :].strip()

                def _cmd(c: str = cmd) -> bool:
                    r = subprocess.run(
                        c,
                        shell=True,
                        cwd=self.root,
                        capture_output=True,
                        text=True,
                        timeout=120,
                        check=False,
                    )
                    return r.returncode == 0

                out.append((name, _cmd))
            else:
                out.append((name, lambda: True))
        return out
