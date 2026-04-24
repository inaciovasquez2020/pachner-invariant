from pathlib import Path

RAW = Path("PachnerInvariant/RawEdgesLocalNodup.lean").read_text()
DOC = Path("docs/math/RAW_EDGES_LOCAL_NODUP_FRONTIER.md").read_text()
NEXT = Path("docs/math/PACHNER_NEXT_SOLVE.md").read_text()

def test_tet_normalized_count_to_any_theorem_exists():
    assert "theorem tet_normalized_count_eq_boolToNat_any" in RAW
    assert "Bool.toNat ((tetToEdges t).any" in RAW
    assert "import PachnerInvariant.frontier" not in RAW

def test_local_count_to_any_status_closed():
    assert "Status: THEOREM-LEVEL LOCAL COUNT-TO-ANY CLOSED." in DOC
    assert "tet_normalized_count_eq_boolToNat_any" in DOC
    assert "No global multiplicity-count closure is claimed yet" in DOC

def test_next_solve_is_global_flatmap_lift():
    assert "Status: OPEN." in NEXT
    assert "Lift the single-tetrahedron count-to-any theorem over `T.tets`" in NEXT
    assert "rawEdges_count_eq_edgeDeg_countP" in NEXT
    assert "No global multiplicity-count closure is claimed" in NEXT
