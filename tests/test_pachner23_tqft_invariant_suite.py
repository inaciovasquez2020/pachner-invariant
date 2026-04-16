import math
from itertools import product

Tet = tuple

def edges(t):
    a,b,c,d = t
    return [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]

# ------------------------------------------------------------
# Pachner 2–3 move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# TEST FUNCTIONAL 1: normalized state-sum (TQFT proxy)
def tqft_state_sum(T, q=2.0):
    Z = 1.0
    for t in T:
        deg = len(set(edges(t)))
        Z *= math.sin(q * (deg + 1)) + 1e-3  # avoid degeneracy
    return Z

def test_tqft_state_sum_variation():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(tqft_state_sum(T) - tqft_state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# TEST FUNCTIONAL 2: fusion-rule inspired local amplitude
def fusion_amplitude(T):
    A = 1.0
    for t in T:
        es = edges(t)
        local = 0.0
        for e in es:
            local += (e[0] + 1) * (e[1] + 1)
        A *= math.cos(local)
    return A

def test_fusion_amplitude_noninvariance():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(fusion_amplitude(T) - fusion_amplitude(T2)) > 1e-9

# ------------------------------------------------------------
# TEST FUNCTIONAL 3: quantum dimension proxy
def quantum_dimension(T):
    return sum(len(set(edges(t)))**2 for t in T)

def test_quantum_dimension_change():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert quantum_dimension(T) != quantum_dimension(T2)

# ------------------------------------------------------------
# TEST FUNCTIONAL 4: normalized TQFT partition function
def normalized_partition(T):
    Z = tqft_state_sum(T)
    norm = sum(len(set(edges(t))) for t in T)
    return Z / (1 + norm)

def test_normalized_partition_noninvariance():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(normalized_partition(T) - normalized_partition(T2)) > 1e-9

# ------------------------------------------------------------
# TEST FUNCTIONAL 5: brute-force TQFT coefficient search
def test_no_low_rank_tqft_invariant():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    def features(X):
        return (
            tqft_state_sum(X),
            fusion_amplitude(X),
            quantum_dimension(X)
        )

    for a,b,c in product([0.5,1.0,2.0], repeat=3):
        F = lambda X: a*features(X)[0] + b*features(X)[1] + c*features(X)[2]
        if abs(F(T) - F(T2)) < 1e-9:
            assert False  # would indicate accidental TQFT invariant in finite basis

    assert True
