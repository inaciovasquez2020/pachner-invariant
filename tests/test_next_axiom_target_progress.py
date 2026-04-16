from pathlib import Path

def test_next_axiom_target_progress():
    s = Path("PachnerInvariant/tests/test_allEdges_count_eq_edgeDeg_countP_stub.lean").read_text()
    assert "#check count_allEdges_eq_filter_tets_len" in s
    assert "#check edgeDeg_eq_incidence_count" in s
    assert "#check count_edgesOfTet_eq_indicator" in s
    assert "allEdges_count_eq_edgeDeg_countP_stub" not in s
