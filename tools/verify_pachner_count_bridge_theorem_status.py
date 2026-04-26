#!/usr/bin/env python3
from pathlib import Path

doc = Path("docs/status/PACHNER_COUNT_BRIDGE_THEOREM_STATUS_2026_04_26.md").read_text(encoding="utf-8")
lean = Path("PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean").read_text(encoding="utf-8")
frontier = Path("PachnerInvariant/frontier.lean").read_text(encoding="utf-8")

required_doc = [
    "Status: Theorem-level bridge synchronized",
    "allEdges_count_eq_edgeDeg_countP",
    "PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean",
    "PachnerInvariant/frontier.lean",
    "allEdges_pachner23_count_delta",
    "edgeDeg_pachner23_delta",
    "edgeDeg_pachner23_eq_expected",
    "Lean build: PASS",
    "pytest: 295/295 passed",
    "commit: ff390fc docs(pachner): sync count bridge theorem status",
    "No global Pachner descent theorem is asserted here.",
    "No new topological invariant theorem is asserted here.",
]

missing = [s for s in required_doc if s not in doc]
assert not missing, "Missing Pachner count-bridge status literals:\n" + "\n".join(missing)

assert "theorem allEdges_count_eq_edgeDeg_countP" in lean

for s in [
    "import PachnerInvariant.allEdges_count_eq_edgeDeg_countP",
    "theorem allEdges_pachner23_count_delta",
    "theorem edgeDeg_pachner23_delta",
    "theorem edgeDeg_pachner23_eq_expected",
]:
    assert s in frontier, f"Missing frontier theorem/import literal: {s}"

for forbidden in [
    "axiom allEdges_count_eq_edgeDeg_countP",
    "count bridge remains axiomatic",
    "global Pachner descent theorem is proved",
    "topological invariant theorem is proved",
]:
    assert forbidden not in doc, f"Forbidden overclaim/stale literal present: {forbidden}"

print("Pachner count bridge theorem status PASS")
