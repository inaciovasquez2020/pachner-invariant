import numpy as np

from PachnerInvariant.pachner_chain_complex import (
    build_chain_complex,
    boundary_operator_1,
    boundary_operator_2,
    kernel_basis_B1,
    image_basis_B2,
    kernel_dimension_B1,
    rank_B2,
    cohomology_H0_dimension,
    cohomology_H1_dimension,
    explicit_H1_representative,
    vector_in_span,
)

def test_chain_complex_builds():
    cc = build_chain_complex()
    assert len(cc.vertices) >= 3
    assert len(cc.edges) >= 6
    assert len(cc.faces) >= 3

def test_boundary_shapes():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    B2 = boundary_operator_2(cc)
    assert B1.shape == (len(cc.vertices), len(cc.edges))
    assert B2.shape == (len(cc.edges), len(cc.faces))

def test_chain_identity_B1_B2_zero():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    B2 = boundary_operator_2(cc)
    assert np.array_equal(B1 @ B2, np.zeros((B1.shape[0], B2.shape[1]), dtype=int))

def test_kernel_basis_explicit():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    basis = kernel_basis_B1(cc)
    assert len(basis) >= 1
    for v in basis:
        assert np.array_equal(B1 @ v, np.zeros(B1.shape[0], dtype=int))

def test_image_B2_lies_in_kernel_B1():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    for v in image_basis_B2(cc):
        assert np.array_equal(B1 @ v, np.zeros(B1.shape[0], dtype=int))

def test_rank_B2_bounded_by_kernel_dimension():
    cc = build_chain_complex()
    assert rank_B2(cc) <= kernel_dimension_B1(cc)

def test_image_spans_cycle_relations_in_kernel():
    cc = build_chain_complex()
    im_basis = image_basis_B2(cc)
    for v in im_basis:
        assert vector_in_span(v, im_basis)

def test_H0_dimension_nonnegative():
    cc = build_chain_complex()
    assert cohomology_H0_dimension(cc) >= 0

def test_H1_dimension_formula():
    cc = build_chain_complex()
    h1 = cohomology_H1_dimension(cc)
    kdim = kernel_dimension_B1(cc)
    r2 = rank_B2(cc)
    assert h1 == kdim - r2
    assert h1 >= 0

def test_detect_explicit_H1_representative():
    cc = build_chain_complex()
    w = explicit_H1_representative(cc)
    if cohomology_H1_dimension(cc) > 0:
        assert w is not None
        assert not vector_in_span(w, image_basis_B2(cc))
        B1 = boundary_operator_1(cc)
        assert np.array_equal(B1 @ w, np.zeros(B1.shape[0], dtype=int))
    else:
        assert w is None
