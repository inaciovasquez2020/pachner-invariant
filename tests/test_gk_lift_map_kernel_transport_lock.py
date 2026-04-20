from pathlib import Path

def test_lift_map_doc_lock() -> None:
    s = Path("docs/math/GK_LIFT_MAP_AND_KERNEL_TRANSPORT.md").read_text()
    assert "## Status" in s
    assert "CONDITIONAL" in s
    assert "\\Phi_k" in s
    assert "Kernel transport invariance" in s
    assert "New-carrier escape" in s
    assert "Pivot collision bound" in s
    assert "Inductive closure lemma" in s

def test_lean_lift_lock() -> None:
    s = Path("PachnerInvariant/GkLift.lean").read_text()
    assert "def liftRow" in s
    assert "def liftRowSpace" in s
    assert "def kernelTransportInvariant" in s
    assert "def newCarrierOutsideTransportedSpan" in s
    assert "def pivotCollisionFree" in s
    assert "theorem allRowsLifted_true" in s
    assert "theorem lifted_kernel_membership" in s
