from pathlib import Path

def test_next_proof_target_lock():
 d = Path("docs/math/NEXT_PROOF_TARGET.md").read_text()
 assert "tetToEdges_normalized_has_length_six" in d
 assert "length = 6" in d
 assert "single-tetrahedron uniqueness bound" in d
