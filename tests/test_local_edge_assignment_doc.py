from pathlib import Path

def test_local_edge_assignment_doc():
    s = Path("docs/math/LOCAL_EDGE_ASSIGNMENT.md").read_text()
    assert "{a,b}" in s
    assert "{p,q}" in s
    assert "Δ = +1" in s
