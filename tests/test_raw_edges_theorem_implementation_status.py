from pathlib import Path

RAW = Path("PachnerInvariant/RawEdgesCommon.lean").read_text()
COUNT = Path("PachnerInvariant/RawEdgesCount.lean").read_text()
DOC = Path("docs/math/RAW_EDGES_THEOREM_IMPLEMENTATION_STATUS.md").read_text()

def test_raw_edges_objects_exist():
    assert "def rawEdges" in RAW
    assert "def pairwiseDistinctTet" in RAW
    assert "def WellFormedTets" in RAW
    assert "theorem rawEdges_def" in RAW
    assert "theorem allEdges_eq_rawEdges_eraseDups" in RAW
    assert "import PachnerInvariant.RawEdgesCommon" in COUNT

def test_raw_edges_status_is_conditional():
    assert "Status: CONDITIONAL." in DOC
    assert "requires `WellFormedTets T`" in DOC
    assert "allEdges = rawEdges.eraseDups" in DOC
    assert "No theorem-level multiplicity-count closure is claimed" in DOC
