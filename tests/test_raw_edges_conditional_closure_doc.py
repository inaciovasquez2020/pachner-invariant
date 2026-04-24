from pathlib import Path

DOC = Path("docs/math/RAW_EDGES_CONDITIONAL_CLOSURE.md").read_text()

def test_raw_edges_replacement_is_conditional():
    assert "Status: Conditional." in DOC
    assert "The old bridge" in DOC
    assert "is false" in DOC
    assert "def rawEdges" in DOC
    assert "def WellFormedTets" in DOC
    assert "theorem rawEdges_count_eq_edgeDeg_countP" in DOC
    assert "propagate `WellFormedTets`" in DOC
