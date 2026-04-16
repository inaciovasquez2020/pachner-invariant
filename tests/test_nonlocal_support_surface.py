from pathlib import Path

def test_nonlocal_support_surface():
    s = Path("PachnerInvariant/nonlocal_support.lean").read_text()
    assert "isNonLocalEdge" in s
    assert "nonlocal_edge_incidence_zero" in s
