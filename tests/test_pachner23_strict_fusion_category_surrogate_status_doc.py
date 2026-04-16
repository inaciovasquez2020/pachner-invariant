from pathlib import Path

def test_pachner23_strict_fusion_category_surrogate_status_doc():
    s = Path("docs/status/PACHNER23_STRICT_FUSION_CATEGORY_SURROGATE_STATUS.md").read_text()
    assert "Linear cochain invariants: classified" in s
    assert "Polynomial invariants: ruled out" in s
    assert "Nonlinear local models: ruled out" in s
    assert "State-sum surrogates: fail invariance" in s
    assert "Categorical proxies: fail axioms" in s
    assert "Strict fusion-category surrogate: fails associativity, closure, coherence, and Pachner 2-3 invariance" in s
    assert "OPEN FOR GENUINE FUSION-CATEGORY INPUT ONLY." in s
