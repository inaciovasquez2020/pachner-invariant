from pathlib import Path

def test_A1_local_edge_count_01_lock():
 d = Path("docs/math/A1_LOCAL_EDGE_COUNT_01.md").read_text()
 assert "allEdges_count_eq_edgeDeg_countP" in d
 assert "List.count (normalizeEdge e) (tetToEdges t) = 0 ∨" in d
 assert "List.count (normalizeEdge e) (tetToEdges t) = 1" in d
