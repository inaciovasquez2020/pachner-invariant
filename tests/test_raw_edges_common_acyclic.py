from pathlib import Path

COMMON = Path("PachnerInvariant/RawEdgesCommon.lean").read_text()
COUNT = Path("PachnerInvariant/RawEdgesCount.lean").read_text()
DOC = Path("docs/math/PACHNER_NEXT_SOLVE.md").read_text()

def test_raw_edges_common_exports_shared_objects():
    assert "def rawEdges" in COMMON
    assert "def pairwiseDistinctTet" in COMMON
    assert "def WellFormedTets" in COMMON
    assert "theorem allEdges_eq_rawEdges_eraseDups" in COMMON

def test_raw_edges_count_imports_common():
    assert "import PachnerInvariant.RawEdgesCommon" in COUNT

def test_next_solve_open_without_multiplicity_claim():
    assert "Status: OPEN." in DOC
    assert "Prove `normalizeEdge_eq_iff`" in DOC
    assert "No multiplicity-count closure is claimed." in DOC
