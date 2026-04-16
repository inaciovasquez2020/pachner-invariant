from PachnerInvariant.pachner_chain_complex import (
    build_chain_complex,
    boundary_operator_1,
    boundary_operator_2,
    cohomology_H0_dimension,
    cohomology_H1_dimension,
)

def test_chain_complex_builds():
    cc = build_chain_complex()
    assert len(cc.vertices) >= 1
    assert len(cc.edges) >= 1

def test_boundary_shapes():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    B2 = boundary_operator_2(cc)
    assert B1.shape[0] == len(cc.vertices)
    assert B2.shape[0] == len(cc.edges)

def test_cohomology_dimensions():
    cc = build_chain_complex()
    h0 = cohomology_H0_dimension(cc)
    h1 = cohomology_H1_dimension(cc)
    assert h0 >= 0
    assert h1 >= 0
