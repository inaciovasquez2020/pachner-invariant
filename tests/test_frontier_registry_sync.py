from pathlib import Path

def test_frontier_registry_sync():
    s = Path("PachnerInvariant/frontier.lean").read_text()
    assert "import PachnerInvariant.allEdges_count_eq_edgeDeg_countP" in s
    assert "import PachnerInvariant.descent_property" in s
    assert "namespace PachnerInvariant" in s
