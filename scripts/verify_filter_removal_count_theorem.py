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

if "theorem erase_length_strictly_smaller" not in proof_text:
    raise SystemExit("missing theorem erase_length_strictly_smaller")

if "have hlen := filter_removal_count_delta xs x h" not in proof_text:
    raise SystemExit("erase_length_strictly_smaller is not gated by filter_removal_count_delta")

if "theorem erase_length_ne_length" not in proof_text:
    raise SystemExit("missing theorem erase_length_ne_length")

if "have hlt := erase_length_strictly_smaller xs x h" not in proof_text:
    raise SystemExit("erase_length_ne_length is not gated by erase_length_strictly_smaller")

if "theorem erase_ne_self_of_mem" not in proof_text:
    raise SystemExit("missing theorem erase_ne_self_of_mem")

if "exact erase_length_ne_length xs x h hlen" not in proof_text:
    raise SystemExit("erase_ne_self_of_mem is not gated by erase_length_ne_length")

if "theorem erase_eq_self_iff_not_mem" not in proof_text:
    raise SystemExit("missing theorem erase_eq_self_iff_not_mem")

if "exact erase_ne_self_of_mem xs x hx h" not in proof_text:
    raise SystemExit("erase_eq_self_iff_not_mem is not gated by erase_ne_self_of_mem")

if "theorem erase_ne_self_iff_mem" not in proof_text:
    raise SystemExit("missing theorem erase_ne_self_iff_mem")

if "erase_eq_self_iff_not_mem xs x" not in proof_text:
    raise SystemExit("erase_ne_self_iff_mem is not gated by erase_eq_self_iff_not_mem")

if "import PachnerInvariant.FilterRemovalCount" not in main_text:
    raise SystemExit("main build does not import PachnerInvariant.FilterRemovalCount")

for token in ("sorry", "admit", "axiom"):
    if re.search(rf"\b{token}\b", proof_text):
        raise SystemExit(f"forbidden token in theorem file: {token}")

print("filter-removal count theorem audit: PASS")
