from pathlib import Path

def test_axiom_replacement_progress():
    s = Path("PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean").read_text()
    assert "count_eq_edgeDeg" in s
    assert "edgeDeg T e" in s
