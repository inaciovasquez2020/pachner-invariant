from pathlib import Path

def test_support_separation_doc_lock() -> None:
    s = Path("docs/math/GK_SUPPORT_SEPARATION_FINAL_WALL.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "Minimal missing lemma" in s
    assert "Finish condition" in s

def test_support_separation_lean_lock() -> None:
    s = Path("PachnerInvariant/GkSupportSeparation.lean").read_text()
    assert "def SupportSeparated" in s
    assert "def FinalWallCleared" in s
    assert "theorem support_separation_implies_final_wall_clear" in s
