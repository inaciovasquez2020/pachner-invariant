from pathlib import Path

def test_tetToEdges_normalized_no_collision_status():
 d = Path("docs/math/TET_TO_EDGES_NORMALIZED_NO_COLLISION_STATUS.md").read_text()
 assert "Not theorem-level verified" in d
 assert "normalizeEdge_eq_iff" in d
 assert "Do not mark tetToEdges_normalized_no_collision as verified" in d
