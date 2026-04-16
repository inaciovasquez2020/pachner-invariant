from pathlib import Path

def test_edge_incidence_range():
    s = Path("PachnerInvariant/edge_incidence_delta.lean").read_text()
    assert "EdgeDelta" in s
    assert "neg2" in s
    assert "pos2" in s
