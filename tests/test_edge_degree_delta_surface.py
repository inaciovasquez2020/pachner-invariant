from pathlib import Path

def test_edge_degree_delta_surface():
    s = Path("PachnerInvariant/edge_degree_delta.lean").read_text()
    assert "edgeDegreeDelta" in s
    assert "edge_degree_delta_lemma" in s
