from pathlib import Path

def test_next_axiom_target_doc():
    s = Path("docs/status/NEXT_AXIOM_TARGET.md").read_text()
    assert "Status: OPEN" in s
    assert "`allEdges_count_eq_edgeDeg_countP`" in s
    assert "edge-count / edge-degree bridge" in s
