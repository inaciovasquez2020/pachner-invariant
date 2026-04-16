from pathlib import Path

def test_local_edge_classes_surface():
    s = Path("PachnerInvariant/local_edge_classes.lean").read_text()
    assert "inductive LocalEdgeClass" in s
    assert "def localEdgeClass" in s
    assert "def edgeDeltaValue" in s
    assert "theorem edgeDeltaValue_range" in s
