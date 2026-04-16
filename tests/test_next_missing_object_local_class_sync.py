from pathlib import Path

def test_next_missing_object_local_class_sync():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "localEdgeClass" in s
    assert "edgeDeltaValue" in s
    assert "ΔΘ expansion theorem" in s
