from pathlib import Path

def test_next_axiom_target_progress():
    s = Path("PachnerInvariant/tests/test_allEdges_count_eq_edgeDeg_countP_stub.lean").read_text()
    assert "allEdges_count_eq_edgeDeg_countP_stub" in s
    assert "edgeDeg T e" in s
