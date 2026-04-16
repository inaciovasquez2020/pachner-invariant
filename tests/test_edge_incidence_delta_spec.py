from pathlib import Path

def test_edge_incidence_delta_spec():
    s = Path("docs/math/EDGE_INCIDENCE_DELTA_SPEC.md").read_text()
    assert "Δ_inc(e)" in s
    assert "Pachner 2→3 move" in s
    assert "local move region" in s
