from pathlib import Path

def test_edge_incidence_delta_surface():
    s = Path("PachnerInvariant/edge_incidence_delta.lean").read_text()
    assert "edgeIncidenceDelta" in s
    assert "edge_incidence_delta_lemma" in s
