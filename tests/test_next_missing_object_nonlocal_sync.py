from pathlib import Path

def test_next_missing_object_nonlocal_sync():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "nonlocal_edge_incidence_zero" in s
