from pathlib import Path


def test_general_2_3_frontier_is_open_and_precise():
    text = Path("docs/math/PACHNER23_GENERAL_2_3_FRONTIER.md").read_text(encoding="utf-8")
    assert "Status: Open." in text
    assert "theorem edgeDeg_pachner23_eq_expected" in text
    assert "acyclic Lean placement" in text


def test_no_failed_closure_module_left_in_package_tree():
    assert not Path("PachnerInvariant/Pachner23MathematicalClosure.lean").exists()
    assert not Path("PachnerInvariant/count_eq_edgeDeg_step1.lean").exists()
    assert not Path("PachnerInvariant/count_eq_edgeDeg_step2.lean").exists()
    assert not Path("tests/test_pachner23_mathematical_closure.py").exists()
