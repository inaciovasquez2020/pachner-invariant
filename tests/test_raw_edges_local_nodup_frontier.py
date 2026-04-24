from pathlib import Path

LOWER = Path("PachnerInvariant/NormalizeEdgeNoCollision.lean").read_text()
DOC = Path("docs/math/RAW_EDGES_LOCAL_NODUP_FRONTIER.md").read_text()

def test_lower_module_contains_normalize_edge_eq_iff():
    assert "theorem normalizeEdge_eq_iff" in LOWER
    assert "theorem normalizeEdge_idem" in LOWER
    assert "import PachnerInvariant.descent_property" in LOWER
    assert "import PachnerInvariant.frontier" not in LOWER

def test_raw_edges_local_nodup_frontier_is_partial():
    assert "Status: PARTIAL THEOREM-LEVEL PROGRESS." in DOC
    assert "Closed lower-module theorem" in DOC
    assert "Remaining theorem-level obligation" in DOC
    assert "theorem tetToEdges_normalized_no_collision" in DOC
    assert "No multiplicity-count closure is claimed yet" in DOC
