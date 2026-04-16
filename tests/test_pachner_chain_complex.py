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
    cohomology_H1_dimension_Z_free,
    cohomology_H1_dimension_Q,
    explicit_H1_representative,
    vector_in_span,
    smith_data_B1,
    smith_data_B2,
    smith_data_H1_presentation,
    homology_H1_torsion_invariants,
    torsion_witness,
)

def test_chain_complex_builds():
    cc = build_chain_complex()
    assert len(cc.vertices) >= 5
    assert len(cc.edges) >= 18
    assert len(cc.faces) >= 12

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
    assert len(basis) >= 3
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
        assert vector_in_span(v, im_basis, domain="Q")

def test_H0_dimension_nonnegative():
    cc = build_chain_complex()
    assert cohomology_H0_dimension(cc) >= 0

def test_H1_dimensions_compare():
    cc = build_chain_complex()
    h1_q = cohomology_H1_dimension_Q(cc)
    h1_z_free = cohomology_H1_dimension_Z_free(cc)
    assert h1_q >= 0
    assert h1_z_free >= 0
    assert h1_q >= h1_z_free

def test_detect_explicit_H1_representative():
    cc = build_chain_complex()
    w = explicit_H1_representative(cc)
    if cohomology_H1_dimension_Q(cc) > 0:
        assert w is not None
        assert not vector_in_span(w, image_generators_B2(cc), domain="Q")
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

def test_smith_normal_form_H1_presentation():
    cc = build_chain_complex()
    D, diag, free_rank = smith_data_H1_presentation(cc)
    assert D.rows == kernel_dimension_B1(cc)
    assert free_rank >= 0
    for d in diag:
        assert isinstance(d, int)
        assert d != 0

def test_detect_torsion_over_Z():
    cc = build_chain_complex()
    torsion = homology_H1_torsion_invariants(cc)
    assert isinstance(torsion, list)
    for d in torsion:
        assert isinstance(d, int)
        assert d >= 2

def test_torsion_witness_format():
    cc = build_chain_complex()
    witness = torsion_witness(cc)
    if witness is not None:
        k, w = witness
        assert isinstance(k, int)
        assert k >= 2
        B1 = boundary_operator_1(cc)
        assert B1 * w == sp.zeros(B1.rows, 1)
