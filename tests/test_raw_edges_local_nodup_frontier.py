from pathlib import Path

DOC = Path("docs/math/RAW_EDGES_LOCAL_NODUP_FRONTIER.md").read_text()

def test_raw_edges_local_nodup_frontier_records_import_cycle():
    assert "Status: BLOCKED BY IMPORT CYCLE." in DOC
    assert "pairwiseDistinctTet_normalized_edges_pairwise" in DOC
    assert "tetToEdges_normalized_no_collision" in DOC
    assert "frontier" in DOC
    assert "build cycle" in DOC
    assert "Move `normalizeEdge_eq_iff` and `tetToEdges_normalized_no_collision`" in DOC
    assert "No multiplicity-count closure is claimed yet" in DOC
