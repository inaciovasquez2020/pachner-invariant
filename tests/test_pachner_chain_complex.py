import sympy as sp

from PachnerInvariant.pachner_chain_complex import (
    build_chain_complex,
    boundary_operator_1,
    boundary_operator_2,
    kernel_basis_B1,
    image_generators_B2,
    kernel_dimension_B1,
    rank_B2,
    cohomology_H0_dimension,
    cohomology_H1_dimension,
    explicit_H1_representative,
    vector_in_span,
    smith_data_B1,
    smith_data_B2,
    homology_H1_torsion_invariants,
)

def test_chain_complex_builds():
    cc = build_chain_complex()
    assert len(cc.vertices) >= 4
    assert len(cc.edges) >= 12
    assert len(cc.faces) >= 9

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
    assert B1 * B2 == sp.zeros(B1.rows, B2.cols)

def test_kernel_basis_explicit():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    basis = kernel_basis_B1(cc)
    assert len(basis) >= 2
    for v in basis:
        assert B1 * v == sp.zeros(B1.rows, 1)

def test_image_B2_lies_in_kernel_B1():
    cc = build_chain_complex()
    B1 = boundary_operator_1(cc)
    for v in image_generators_B2(cc):
        assert B1 * v == sp.zeros(B1.rows, 1)

def test_rank_B2_bounded_by_kernel_dimension():
    cc = build_chain_complex()
    assert rank_B2(cc) <= kernel_dimension_B1(cc)

def test_image_spans_its_cycle_relations():
    cc = build_chain_complex()
    im_basis = image_generators_B2(cc)
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
        assert not vector_in_span(w, image_generators_B2(cc))
        B1 = boundary_operator_1(cc)
        assert B1 * w == sp.zeros(B1.rows, 1)
    else:
        assert w is None

def test_smith_normal_form_kernel_data():
    cc = build_chain_complex()
    D, diag = smith_data_B1(cc)
    assert D.shape == boundary_operator_1(cc).shape
    assert len(diag) == boundary_operator_1(cc).rank()

def test_smith_normal_form_image_data():
    cc = build_chain_complex()
    D, diag = smith_data_B2(cc)
    assert D.shape == boundary_operator_2(cc).shape
    assert len(diag) == boundary_operator_2(cc).rank()

def test_detect_torsion_over_Z():
    cc = build_chain_complex()
    torsion = homology_H1_torsion_invariants(cc)
    assert isinstance(torsion, list)
    for d in torsion:
        assert isinstance(d, int)
        assert d >= 2
