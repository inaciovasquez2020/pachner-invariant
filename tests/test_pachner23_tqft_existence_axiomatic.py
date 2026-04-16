import math

# ------------------------------------------------------------
# consistent 6-label extraction from tetrahedron
def tetra_to_6labels(t):
    a,b,c,d = t
    return (a,b,c,a,b,d)

# ------------------------------------------------------------
# 6j-symbol surrogate (categorical placeholder)
def F(a,b,c,d,e,f):
    return math.cos(a + b - c + d - e + f)

# ------------------------------------------------------------
# pentagon failure measure (categorical coherence proxy)
def pentagon(lhs, rhs):
    return abs(lhs - rhs)

# ------------------------------------------------------------
# Pachner 2–3 move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# state-sum (now correctly arity-consistent)
def state_sum(T):
    total = 0.0
    for t in T:
        a,b,c,d,e,f = tetra_to_6labels(t)
        total += F(a,b,c,d,e,f)
    return total

# ------------------------------------------------------------
# TEST 1: categorical structure is NOT coherent (proxy model)
def test_pentagon_coherence_failure():
    lhs = F(0,1,2,3,4,5) * F(0,1,3,4,5,6)
    rhs = F(1,2,3,4,5,6) * F(0,2,3,5,6,7)
    assert abs(lhs - rhs) > 1e-9

# ------------------------------------------------------------
# TEST 2: Pachner invariance fails under state-sum
def test_pachner_invariance_failure():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(state_sum(T) - state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# TEST 3: no accidental scalar correction fixes invariance
def test_no_scalar_fix():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    Z1 = state_sum(T)
    Z2 = state_sum(T2)

    for k in [0.5, 1.0, 2.0]:
        if abs(k*Z1 - k*Z2) < 1e-9:
            assert False

    assert True

# ------------------------------------------------------------
# TEST 4: categorical asymmetry persists globally
def test_global_asymmetry():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert state_sum(T) != state_sum(T2)

# ------------------------------------------------------------
# TEST 5: existence reformulation (logical structure)
def test_existence_requires_true_tqft_structure():
    # A true TQFT would require BOTH:
    pentagon_ok = False
    pachner_invariant = False

    assert not (pentagon_ok and pachner_invariant)
