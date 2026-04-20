from pathlib import Path

def test_inductive_independence_doc_lock() -> None:
    s = Path("docs/math/GK_INDUCTIVE_INDEPENDENCE_PRESERVATION.md").read_text()
    assert "## Status" in s
    assert "CONDITIONAL" in s
    assert "Carrier support disjointness" in s
    assert "Lift injectivity on the old certified space" in s
    assert "Kernel direct-sum transport" in s
    assert "Intersection equality" in s
    assert "inductive_independence_preservation" in s

def test_inductive_independence_lean_lock() -> None:
    s = Path("PachnerInvariant/GkInductiveIndependence.lean").read_text()
    assert "def supportDisjointFromPivotAndKernel" in s
    assert "def InjectiveOnLift" in s
    assert "def KernelDirectSumTransport" in s
    assert "def IntersectionEqualityHolds" in s
    assert "theorem injective_on_lift_certified_space" in s
    assert "theorem kernel_direct_sum_transport_of_membership" in s
    assert "theorem inductive_independence_preservation" in s
