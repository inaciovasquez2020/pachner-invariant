from pathlib import Path

def test_edge_incidence_case_split_doc():
    s = Path("docs/math/EDGE_INCIDENCE_CASE_SPLIT.md").read_text()
    assert "Δ_inc(e)" in s
    assert "{-2,-1,0,1,2}" in s
