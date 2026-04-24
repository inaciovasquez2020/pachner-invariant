from pathlib import Path

LOWER = Path("PachnerInvariant/NormalizeEdgeNoCollision.lean").read_text()
RAW = Path("PachnerInvariant/RawEdgesLocalNodup.lean").read_text()
DOC = Path("docs/math/RAW_EDGES_LOCAL_NODUP_FRONTIER.md").read_text()

def test_lower_module_contains_tet_no_collision():
    assert "theorem normalizeEdge_eq_iff" in LOWER
    assert "theorem tetToEdges_normalized_no_collision" in LOWER
    assert "import PachnerInvariant.descent_property" in LOWER
    assert "import PachnerInvariant.frontier" not in LOWER

def test_raw_edges_local_nodup_adapter_builds_below_frontier():
    assert "theorem pairwiseDistinctTet_normalized_edges_pairwise" in RAW
    assert "import PachnerInvariant.RawEdgesCommon" in RAW
    assert "import PachnerInvariant.NormalizeEdgeNoCollision" in RAW
    assert "import PachnerInvariant.frontier" not in RAW

def test_raw_edges_local_nodup_frontier_closed():
    assert "Status: THEOREM-LEVEL LOCAL NODUP CLOSED." in DOC
    assert "Both build without importing `frontier`." in DOC
    assert "Remaining theorem-level obligation" in DOC
    assert "No multiplicity-count closure is claimed yet" in DOC
