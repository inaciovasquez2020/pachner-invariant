from pathlib import Path

def test_next_missing_object_o3_sync():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "edge-degree delta formula" in s
