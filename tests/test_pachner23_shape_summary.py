from pathlib import Path

DOC = Path("docs/math/PACHNER23_SHAPE_SUMMARY.md").read_text()
ART = Path("artifacts/pachner23_shape_summary.txt").read_text()

def test_pachner23_shape_summary_is_inspection_only():
    assert "Status: INSPECTION SUMMARY." in DOC
    assert "theorem WellFormedTets_pachner23" in DOC
    assert "Extract the exact inserted tetrahedron list" in DOC
    assert "No theorem-level closure is claimed by this summary." in DOC
    assert "No false `allEdges` multiplicity bridge is restored." in DOC

def test_pachner23_shape_summary_has_candidate_lines():
    assert "pachner23" in DOC
    assert len(ART.strip()) > 0
