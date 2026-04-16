from PachnerInvariant.pachner_groupoid_sampling import (
    build_groupoid_sample,
    incidence_matrix,
    kernel_dimension,
    rank,
)

def test_groupoid_build():
    sample = build_groupoid_sample()
    assert len(sample.vertices) >= 5
    assert len(sample.edges) >= 10

def test_incidence_matrix():
    sample = build_groupoid_sample()
    B = incidence_matrix(sample)
    assert B.shape[0] == len(sample.vertices)
    assert B.shape[1] == len(sample.edges)

def test_kernel_vs_rank():
    sample = build_groupoid_sample()
    B = incidence_matrix(sample)
    k = kernel_dimension(B)
    r = rank(B)
    assert k >= 0
    assert r >= 0
    assert k + r == B.shape[1]
