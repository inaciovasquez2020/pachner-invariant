from PachnerInvariant.pachner_groupoid_sampling import (
    build_groupoid_sample,
    incidence_matrix,
    path_boundary_matrix,
    kernel_dimension,
    rank,
    connected_components,
)

def test_groupoid_build():
    sample = build_groupoid_sample()
    assert len(sample.vertices) >= 5
    assert len(sample.edges) >= 10
    assert len(sample.paths2) >= 1

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
