from pathlib import Path

LEAN = Path("PachnerInvariant/Pachner23InsertedPairwise.lean").read_text()
DOC = Path("docs/math/PACHNER23_INSERTED_PAIRWISE.md").read_text()
NEXT = Path("docs/math/PACHNER_NEXT_SOLVE.md").read_text()

def test_inserted_pairwise_lemmas_exist():
    assert "theorem pairwiseDistinctTet_abpq" in LEAN
    assert "theorem pairwiseDistinctTet_acpq" in LEAN
    assert "theorem pairwiseDistinctTet_bcpq" in LEAN
    assert "import PachnerInvariant.RawEdgesCommon" in LEAN

def test_inserted_pairwise_status_closed_but_scoped():
    assert "Status: THEOREM-LEVEL INSERTED PAIRWISE SURFACE CLOSED." in DOC
    assert "(a,b,p,q), (a,c,p,q), (b,c,p,q)" in DOC
    assert "This does not prove `WellFormedTets_pachner23`." in DOC
    assert "No false `allEdges` multiplicity bridge is restored." in DOC

def test_next_solve_is_constructor_connection():
    assert "Status: OPEN." in NEXT
    assert "Connect the repository-level `pachner23` constructor" in NEXT
    assert "theorem WellFormedTets_pachner23" in NEXT
    assert "No unconditional Pachner 2--3 delta theorem is claimed." in NEXT
