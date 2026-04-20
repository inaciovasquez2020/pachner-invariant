from __future__ import annotations

from pathlib import Path


def test_closure_boundary_doc_lock() -> None:
    s = Path("docs/math/GK_TRUE_P23_INDUCTIVE_CLOSURE_BOUNDARY.md").read_text()
    assert "## Status" in s
    assert "CONDITIONAL" in s
    assert "Carrier Independence." in s
    assert "Explicit Lift Rule." in s
    assert "Kernel Disjointness Under Lift." in s
    assert "This document does not claim unconditional theorem-level closure." in s


def test_construction_rule_doc_lock() -> None:
    s = Path("docs/math/GK_TRUE_P23_CONSTRUCTION_RULE.md").read_text()
    assert "## Status" in s
    assert "CONDITIONAL" in s
    assert "generator complement" in s
    assert "canonical repository-native replacement" in s


def test_lean_inductive_lemma_lock() -> None:
    s = Path("PachnerInvariant/GkTrueP23.lean").read_text()
    assert "theorem carrierLift_nonzero" in s
    assert "theorem closureBoundary_only_if" in s
    assert "def ClosureBoundarySatisfied" in s
