from __future__ import annotations

import compileall
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(label: str, *args: str) -> None:
    print(f"==> {label}")
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    print(f"UASEP validation root: {ROOT}")
    if not compileall.compile_dir(str(ROOT / "runtime"), quiet=1):
        print("runtime compilation failed", file=sys.stderr)
        return 1

    run(
        "conformance + integration",
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "tests/conformance",
        "tests/integration",
        "tests/test_runtime.py",
    )
    run("full pytest suite", sys.executable, "-m", "pytest", "-q")
    print("UASEP VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
