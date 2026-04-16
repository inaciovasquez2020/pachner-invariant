from pathlib import Path

def test_al2_local_edge_classification_doc():
    s = Path("docs/math/AL2_LOCAL_EDGE_CLASSIFICATION_THEOREM.md").read_text()
    assert "Δ_inc(e)" in s
    assert "Support:" in s
    assert "Range:" in s
    assert "{p,q}" in s
