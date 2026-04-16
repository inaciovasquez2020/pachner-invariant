from PachnerInvariant.pachner_groupoid_sampling import (
    build_groupoid_sample,
    incidence_matrix,
    path_boundary_matrix,
    kernel_dimension,
    rank,
    connected_components,
    cycle_space_dimension,
    H1_dimension,
)

def test_groupoid_build():
    sample = build_groupoid_sample()
    assert len(sample.vertices) >= 7
    assert len(sample.edges) >= 20
    assert len(sample.paths2) >= 5

def test_incidence_matrix():
    sample = build_groupoid_sample()
    B = incidence_matrix(sample)
    assert B.shape[0] == len(sample.vertices)
    assert B.shape[1] == len(sample.edges)

def test_path_boundary_matrix():
    sample = build_groupoid_sample()
    B2 = path_boundary_matrix(sample)
    assert B2.shape[0] == len(sample.edges)
    assert B2.shape[1] == len(sample.paths2)

def test_kernel_vs_rank():
    sample = build_groupoid_sample()
    B = incidence_matrix(sample)
    k = kernel_dimension(B)
    r = rank(B)
    assert k >= 0
    assert r >= 0
    assert k + r == B.shape[1]

def test_connected_components_positive():
    sample = build_groupoid_sample()
    c = connected_components(sample)
    assert c >= 1

def test_cycle_space_dimension():
    sample = build_groupoid_sample()
    d = cycle_space_dimension(sample)
    assert d >= 0

def test_H1_dimension_nonnegative():
    sample = build_groupoid_sample()
    h1 = H1_dimension(sample)
    assert h1 >= 0
