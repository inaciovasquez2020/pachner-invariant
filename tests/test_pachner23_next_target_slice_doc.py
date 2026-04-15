from pathlib import Path

def test_pachner23_next_target_slice_doc():
    s = Path("docs/math/PACHNER23_NEXT_TARGET_SLICE.md").read_text()
    assert "OPEN" in s
    assert "`allEdges_count_eq_edgeDeg_countP`" in s
    assert "edge-count / edge-degree bridge" in s
    assert "`edgeDeg_pachner23_eq_expected`" in s
    assert "No unconditional closure is claimed" in s
