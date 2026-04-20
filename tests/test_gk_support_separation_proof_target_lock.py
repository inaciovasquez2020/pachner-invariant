from pathlib import Path

def test_support_separation_proof_target_doc_lock() -> None:
    s = Path("docs/math/GK_SUPPORT_SEPARATION_PROOF_TARGET.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "Repository-native proof obligations" in s
    assert "Finish condition" in s

def test_support_separation_proof_target_lean_lock() -> None:
    s = Path("PachnerInvariant/GkSupportSeparationTarget.lean").read_text()
    assert "def SupportSeparatedFromPivots" in s
    assert "def SupportSeparatedFromKernelLeads" in s
    assert "def SupportSeparationTarget" in s
