from __future__ import annotations

from pathlib import Path
import json

from pachner_invariant.gk_pachner_boundary import replace_synthetic_with_true_pachner, lift_bounded_g2_to_gk


def test_true_p23_f6_lock() -> None:
    data = replace_synthetic_with_true_pachner("F6", 6)
    assert data["d2out_row_count"] == 3
    assert data["extended_rank"] == 8
    assert data["status"] == "PASS"


def test_true_p23_f7_lock() -> None:
    data = replace_synthetic_with_true_pachner("F7", 7)
    assert data["d2out_row_count"] == 18
    assert data["extended_rank"] == 43
    assert data["status"] == "PASS"


def test_gk_lift_summary_lock() -> None:
    summary = lift_bounded_g2_to_gk(max_k=9)
    assert summary["G8"]["status"] == "INDUCTIVE_TEMPLATE"
    assert summary["G9"]["status"] == "INDUCTIVE_TEMPLATE"


def test_true_p23_artifact_written() -> None:
    replace_synthetic_with_true_pachner("F7", 7)
    p = Path("artifacts/g2_certification/F7_true_p23_extension.json")
    assert p.exists()
    data = json.loads(p.read_text())
    assert data["status"] == "PASS"
