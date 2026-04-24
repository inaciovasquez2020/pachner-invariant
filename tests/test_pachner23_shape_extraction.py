from pathlib import Path

DOC = Path("docs/math/PACHNER23_SHAPE_EXTRACTION.md").read_text()
ART = Path("artifacts/pachner23_shape_extraction.json").read_text()

def test_pachner23_shape_extraction_doc_exists():
    assert "Status: INSPECTION LOCK." in DOC
    assert "identify the exact tetrahedra inserted and removed by `pachner23`" in DOC
    assert "Search target: `pachner23`" in DOC

def test_pachner23_shape_extraction_has_hits_or_explicit_failure():
    assert "hit_count" in ART
    assert ("PachnerInvariant/" in DOC) or ("No `pachner23` occurrence found" in DOC)
