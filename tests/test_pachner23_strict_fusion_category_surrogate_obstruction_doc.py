from pathlib import Path

def test_pachner23_strict_fusion_category_surrogate_obstruction_doc():
    s = Path("docs/math/PACHNER23_STRICT_FUSION_CATEGORY_SURROGATE_OBSTRUCTION.md").read_text()
    assert "Conditional." in s
    assert "fusion category exists" in s
    assert "pentagon identity holds" in s
    assert "Pachner invariance holds" in s
    assert "associativity test fails" in s
    assert "closure test fails" in s
    assert "pentagon/coherence test fails" in s
    assert "Pachner 2-3 invariance test fails" in s
    assert "No finite analytic or algebraic surrogate" in s
    assert "genuine fusion category with strict pentagon coherence" in s
