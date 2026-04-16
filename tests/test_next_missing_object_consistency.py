from pathlib import Path

def test_next_missing_object_consistency():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    t = Path("PachnerInvariant/theta_delta.lean").read_text()
    assert "theta_pachner23_delta" in s
    assert "theta_pachner23_delta" in t
