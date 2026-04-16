from pathlib import Path

def test_next_missing_object_points_to_edge_incidence():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "edge_incidence_delta_lemma" in s
