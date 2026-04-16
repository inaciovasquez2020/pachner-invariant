from pathlib import Path

def test_local_edge_set_surface():
    s = Path("PachnerInvariant/local_edge_set.lean").read_text()
    assert "def isLocalMoveEdge" in s
    assert '(p,q)' in s
