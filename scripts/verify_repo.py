#!/usr/bin/env python3
from pathlib import Path
import sys

required = [
    "README.md",
    "CITATION.cff",
    "Main.lean",
    "PachnerInvariant.lean",
    "lakefile.lean",
    "lean-toolchain",
    "docs",
    "tests",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print({"valid": False, "missing": missing})
    sys.exit(1)

checks = {}

readme = Path("README.md").read_text(errors="ignore").lower()
checks["mentions_pachner"] = "pachner" in readme
checks["mentions_invariant"] = "invariant" in readme
checks["mentions_theta"] = "theta" in readme or "θ" in readme
checks["mentions_frontier"] = "frontier" in readme
checks["mentions_build"] = "lake build" in readme

failed = [k for k, v in checks.items() if not v]
if failed:
    print({"valid": False, "failed_checks": failed, "checks": checks})
    sys.exit(1)

print({"valid": True, "checked": required, "checks": checks})
