from pathlib import Path

def test_thetaZ_blockers_status():
    s = Path("docs/math/THETAZ_BLOCKERS.md").read_text()
    assert "Status: Conditional." in s
    assert "`allEdges_pachner23_eq`" in s
    assert "`allEdges_mem_of_pachner23_new_edge`" in s
    assert "`List.foldl_congr_sub_eq_changed_terms`" in s
    assert "`thetaZ_pachner23_delta_expanded`" in s
