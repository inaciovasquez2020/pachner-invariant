from pathlib import Path

def test_next_proof_target_lock():
 d = Path("docs/math/NEXT_PROOF_TARGET.md").read_text()
 assert "tetToEdges_count_normalizeEdge_le_one" in d
 assert "allEdges_count_eq_edgeDeg_countP" in d
 assert "single-tetrahedron uniqueness bound" in d
