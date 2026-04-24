from pathlib import Path

DOC = Path("docs/math/PACHNER23_INSERTED_TET_REGISTRY.md").read_text()
ART = Path("artifacts/pachner23_inserted_tet_registry.txt").read_text()

def test_pachner23_inserted_tet_registry_locked():
    assert "Status: REGISTRY LOCK." in DOC
    assert "pachner23_inserted_tets_pairwiseDistinct" in DOC
    assert "The exact inserted tetrahedron list must be selected" in DOC
    assert "No theorem-level closure is claimed." in DOC
    assert "No false `allEdges` multiplicity bridge is restored." in DOC

def test_pachner23_inserted_tet_registry_has_candidates():
    assert "pachner23" in DOC
    assert len(ART.strip()) > 0
