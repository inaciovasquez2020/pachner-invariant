from pathlib import Path

def test_next_proof_target_lock():
 d = Path("docs/math/NEXT_PROOF_TARGET.md").read_text()
 assert "tetToEdges_normalized_no_collision_pairwiseDistinct4" in d
 assert "Pairwise (· ≠ ·) es" in d
 assert "terminal obstruction" in d
