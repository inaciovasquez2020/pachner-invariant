from pathlib import Path

def test_local_edge_classification_plan_doc():
    s = Path("docs/math/LOCAL_EDGE_CLASSIFICATION_PLAN.md").read_text()
    assert "LocalEdgeClass" in s
    assert "EdgeDelta" in s
    assert "explicit combinatorial assignment still open" in s
