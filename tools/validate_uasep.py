from __future__ import annotations

import compileall
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Branch `new`: only ideology-aligned tests until legacy suite is fully removed.
UNIFIED_TESTS = [
    "tests/test_runtime.py",
    "tests/conformance/test_unified_graph.py",
    "tests/integration/test_unified_supervisor.py",
    "tests/integration/test_local_cli_adapter.py",
]


def run(label: str, *args: str) -> None:
    print(f"==> {label}")
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    print(f"UASEP validation root: {ROOT}")
    if not compileall.compile_dir(str(ROOT / "runtime"), quiet=1):
        print("runtime compilation failed", file=sys.stderr)
        return 1
    if not compileall.compile_dir(str(ROOT / "adapters"), quiet=1):
        print("adapters compilation failed", file=sys.stderr)
        return 1

    run("unified tests", sys.executable, "-m", "pytest", "-q", *UNIFIED_TESTS)
    print("UASEP VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
