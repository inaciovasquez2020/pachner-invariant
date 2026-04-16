from pathlib import Path

def test_theta_delta_imports_degree_delta():
    s = Path("PachnerInvariant/theta_delta.lean").read_text()
    assert "edge_degree_delta" in s or "edge_degree_delta" in s.lower()
