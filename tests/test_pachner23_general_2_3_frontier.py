from pathlib import Path


def test_general_2_3_frontier_is_complete():
    text = Path("docs/math/PACHNER23_GENERAL_2_3_FRONTIER.md").read_text(encoding="utf-8")
    assert "Status: Complete." in text
    assert "theorem edgeDeg_pachner23_eq_expected" in text
    assert "theorem edgeDeg_pachner23_delta" in text
    assert "theorem allEdges_pachner23_count_delta" in text


def test_general_2_3_no_residual_axiom_frontier():
    text = Path("PachnerInvariant/frontier.lean").read_text(encoding="utf-8")
    assert "theorem edgeDeg_pachner23_eq_expected" in text
    assert "theorem edgeDeg_pachner23_delta" in text
    assert "theorem allEdges_pachner23_count_delta" in text
    assert "axiom edgeDeg_pachner23_eq_expected" not in text
    assert "axiom edgeDeg_pachner23_delta" not in text
    assert "axiom allEdges_count_eq_edgeDeg_countP" not in text
    assert "sorry" not in text


def test_no_failed_closure_module_left_in_package_tree():
    assert not Path("PachnerInvariant/Pachner23MathematicalClosure.lean").exists()
    assert not Path("PachnerInvariant/count_eq_edgeDeg_step1.lean").exists()
    assert not Path("PachnerInvariant/count_eq_edgeDeg_step2.lean").exists()
    assert not Path("tests/test_pachner23_mathematical_closure.py").exists()
