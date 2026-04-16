from pathlib import Path

def test_next_axiom_target_locked():
    s = Path("PachnerInvariant/frontier.lean").read_text()
    assert "import PachnerInvariant.allEdges_count_eq_edgeDeg_countP" in s
    assert "axiom allEdges_count_eq_edgeDeg_countP" not in s
