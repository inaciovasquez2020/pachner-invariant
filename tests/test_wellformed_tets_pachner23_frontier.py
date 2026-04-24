from pathlib import Path

DOC = Path("docs/math/WELLFORMED_TETS_PACHNER23_FRONTIER.md").read_text()
NEXT = Path("docs/math/PACHNER_NEXT_SOLVE.md").read_text()

def test_wellformed_tets_pachner23_frontier_is_open():
    assert "Status: OPEN THEOREM-LEVEL FRONTIER." in DOC
    assert "theorem WellFormedTets_pachner23" in DOC
    assert "Identify the exact tetrahedra inserted and removed by `pachner23`" in DOC
    assert "No unconditional Pachner 2--3 delta theorem is claimed here." in DOC
    assert "No false `allEdges` multiplicity bridge is restored." in DOC

def test_next_solve_still_points_to_wellformed_pachner23():
    assert "Status: OPEN." in NEXT
    assert "Propagate `WellFormedTets` through the Pachner 2--3 move layer." in NEXT
    assert "theorem WellFormedTets_pachner23" in NEXT
