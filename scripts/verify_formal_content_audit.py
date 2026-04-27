#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

proof = root / "PachnerInvariant" / "FilterRemovalCount.lean"
main = root / "PachnerInvariant.lean"

if not proof.exists():
    raise SystemExit("missing PachnerInvariant/FilterRemovalCount.lean")
if not main.exists():
    raise SystemExit("missing PachnerInvariant.lean")

proof_text = proof.read_text(encoding="utf-8")
main_text = main.read_text(encoding="utf-8")

if "theorem filter_removal_count_delta" not in proof_text:
    raise SystemExit("missing theorem filter_removal_count_delta")

if "import PachnerInvariant.FilterRemovalCount" not in main_text:
    raise SystemExit("main build does not import PachnerInvariant.FilterRemovalCount")

for token in ("sorry", "admit", "axiom"):
    if re.search(rf"\b{token}\b", proof_text):
        raise SystemExit(f"forbidden token in theorem file: {token}")

print("formal content audit: PASS")
