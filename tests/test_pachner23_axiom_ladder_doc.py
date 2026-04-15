from pathlib import Path

def test_pachner23_axiom_ladder_doc():
    s = Path("docs/math/PACHNER23_AXIOM_LADDER.md").read_text()
    assert "OPEN" in s
    assert "allEdges_count_eq_edgeDeg_countP" in s
    assert "edge-count / edge-degree bridge" in s
    assert "No unconditional closure is claimed" in s
