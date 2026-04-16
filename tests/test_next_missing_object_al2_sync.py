from pathlib import Path

def test_next_missing_object_al2_sync():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "AL2. Exact local edge-classification theorem." in s
    assert "nonlocal-support theorem" in s
    assert "theta_pachner23_delta" in s
