from pathlib import Path

COMMON = Path("PachnerInvariant/RawEdgesCommon.lean").read_text()
COUNT = Path("PachnerInvariant/RawEdgesCount.lean").read_text()
LOCAL = Path("PachnerInvariant/RawEdgesLocalNodup.lean").read_text()
DOC = Path("docs/math/PACHNER_NEXT_SOLVE.md").read_text()

def test_raw_edges_common_exports_shared_objects():
    assert "def rawEdges" in COMMON
    assert "def pairwiseDistinctTet" in COMMON
    assert "def WellFormedTets" in COMMON
    assert "theorem allEdges_eq_rawEdges_eraseDups" in COMMON

def test_raw_edges_count_imports_common():
    assert "import PachnerInvariant.RawEdgesCommon" in COUNT

def test_local_nodup_is_acyclic_over_common():
    assert "import PachnerInvariant.RawEdgesCommon" in LOCAL
    assert "import PachnerInvariant.RawEdgesCount" not in LOCAL
    assert "import PachnerInvariant.frontier" not in LOCAL

def test_next_solve_open_without_multiplicity_claim():
    assert "Status: OPEN." in DOC
    assert "`tetToEdges_normalized_no_collision` now build" in DOC
    assert "local count-to-any bridge" in DOC
    assert "No multiplicity-count closure is claimed." in DOC
