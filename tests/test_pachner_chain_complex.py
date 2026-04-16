from PachnerInvariant.pachner_chain_complex import (
    build_chain_complex,
    boundary_operator_1,
    cohomology_H0_dimension,
)

def test_chain_complex_builds():
    cc = build_chain_complex()
    assert len(cc.vertices) >= 1
    assert len(cc.edges) >= 1

def test_boundary_operator_shape():
    cc = build_chain_complex()
    B = boundary_operator_1(cc)
    assert B.shape[0] == len(cc.vertices)
    assert B.shape[1] == len(cc.edges)

def test_H0_dimension_nonnegative():
    cc = build_chain_complex()
    h0 = cohomology_H0_dimension(cc)
    assert h0 >= 0
