from pathlib import Path

def test_local_edge_types_surface():
    s = Path("PachnerInvariant/local_edge_types.lean").read_text()
    assert "LocalEdgeType" in s
    assert "deltaOfType" in s
    assert "edgeIncidenceDelta_refined" in s
