from pathlib import Path

LOWER = Path("PachnerInvariant/NormalizeEdgeNoCollision.lean").read_text()

def test_normalize_edge_eq_iff_is_lower_module_theorem():
    assert "theorem normalizeEdge_eq_iff" in LOWER
    assert "import PachnerInvariant.descent_property" in LOWER
    assert "import PachnerInvariant.frontier" not in LOWER
    assert "theorem normalizeEdge_idem" in LOWER
