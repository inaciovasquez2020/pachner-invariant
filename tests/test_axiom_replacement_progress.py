from pathlib import Path

def test_axiom_replacement_progress():
    s = Path("PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean").read_text()
    assert "sum_edgeDeg_eq_sum_counts" in s
    assert "length_eq_sum_edge_counts" in s
    assert "admit" in s
