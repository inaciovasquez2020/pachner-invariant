from pathlib import Path

def test_next_proof_target_lock():
 d = Path("docs/math/NEXT_PROOF_TARGET.md").read_text()
 assert "pairwiseDistinct4_normalizeEdge_injective_on_tetToEdges" in d
 assert "es.Nodup" in d
 assert "duplicate-free under pairwiseDistinct4" in d
