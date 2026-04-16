from pathlib import Path

def test_structural_docs_sync():
    stack = Path("docs/structure/STRUCTURAL_STACK.md").read_text()
    scope = Path("docs/structure/STRUCTURAL_SCOPE.md").read_text()
    graph = Path("docs/structure/DEPENDENCY_GRAPH.md").read_text()
    boundary = Path("docs/status/STRUCTURAL_BOUNDARY.md").read_text()
    iface = Path("docs/structure/PACHNER_MOVE_INTERFACE.md").read_text()
    nxt = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()

    assert "Matveev" in stack
    assert "Pachner 2→3 moves" in scope
    assert "Θ-descent property" in graph
    assert "triangulated 3-manifolds" in boundary
    assert "Valid23" in iface
    assert "theta_pachner23_delta" in nxt
