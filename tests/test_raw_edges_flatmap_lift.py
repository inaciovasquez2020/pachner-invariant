from pathlib import Path

LEAN = Path("PachnerInvariant/RawEdgesFlatMapLift.lean").read_text()
DOC = Path("docs/math/RAW_EDGES_FLATMAP_LIFT.md").read_text()
NEXT = Path("docs/math/PACHNER_NEXT_SOLVE.md").read_text()

def test_raw_edges_global_lift_theorem_exists():
    assert "theorem rawEdges_count_eq_edgeDeg_countP" in LEAN
    assert "(hT : WellFormedTets T)" in LEAN
    assert "rawEdges_count_eq_edgeDeg_countP_aux" in LEAN
    assert "tet_normalized_count_eq_boolToNat_any" in LEAN

def test_raw_edges_global_lift_status_is_conditional():
    assert "Status: CONDITIONAL THEOREM-LEVEL GLOBAL LIFT CLOSED." in DOC
    assert "This is conditional on `WellFormedTets T`." in DOC
    assert "This does not restore the false `allEdges` multiplicity bridge." in DOC
    assert "`allEdges = rawEdges.eraseDups`" in DOC

def test_next_solve_is_wellformed_pachner23():
    assert "Status: OPEN." in NEXT
    assert "`rawEdges_count_eq_edgeDeg_countP` now builds" in NEXT
    assert "Propagate `WellFormedTets` through the Pachner 2--3 move layer." in NEXT
    assert "theorem WellFormedTets_pachner23" in NEXT
