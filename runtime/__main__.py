from __future__ import annotations

import argparse
from pathlib import Path

from .capabilities import CapabilityRegistry
from .state import StateStore


def main() -> int:
    parser = argparse.ArgumentParser(description="UASEP reference runtime diagnostics")
    parser.add_argument("project", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.project).resolve()
    store = StateStore(root)
    state = store.load(root.name)
    registry = CapabilityRegistry.empty()
    print(f"UASEP 3.1.0 | project={root}")
    print(f"state.phase={state.phase} iteration={state.iteration}")
    print("capabilities=" + ",".join(name for name, cap in registry.capabilities.items() if cap.available) or "none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
