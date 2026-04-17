from pathlib import Path

def test_thetaz_remaining_bridges_status():
    s = Path("docs/math/THETAZ_REMAINING_BRIDGES.md").read_text(encoding="utf-8")
    assert "Status: Conditional." in s
    assert "`allEdges_mem_of_pachner23_new_edge`" in s
    assert "`thetaZ_eq_theta_cast`" in s
