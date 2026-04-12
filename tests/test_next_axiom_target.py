from pathlib import Path

def test_next_axiom_target_locked():
 s = Path("PachnerInvariant/frontier.lean").read_text()
 assert "axiom allEdges_count_eq_edgeDeg_countP" in s
 d = Path("docs/math/NEXT_AXIOM_TARGET.md").read_text()
 assert "allEdges_count_eq_edgeDeg_countP" in d
 assert "Replace allEdges_count_eq_edgeDeg_countP by a proved theorem" in d
