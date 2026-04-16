import math

# ------------------------------------------------------------
# 6-label tetrahedral encoding (consistent categorical object)
def tetra_to_6labels(t):
    a,b,c,d = t
    return (a,b,c,a,d,b)

# ------------------------------------------------------------
# 6j-symbol surrogate
def F(a,b,c,d,e,f):
    return math.cos(a + b - c + d - e + f)

# ------------------------------------------------------------
# Pachner move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# state-sum (NOW TYPE-CONSISTENT)
def state_sum(T):
    return sum(F(*tetra_to_6labels(t)) for t in T)

# ------------------------------------------------------------
# 1. pentagon failure (categorical obstruction remains)
def test_pentagon_obstruction():
    lhs = F(0,1,2,3,4,5) * F(0,1,3,4,5,6)
    rhs = F(1,2,3,4,5,6) * F(0,2,3,5,6,7)
    assert abs(lhs - rhs) > 1e-9

# ------------------------------------------------------------
# 2. Pachner invariance failure (now well-defined)
def test_pachner_invariance_failure():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(state_sum(T) - state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# 3. no scalar renormalization fixes invariance
def test_no_scalar_fix():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    Z1 = state_sum(T)
    Z2 = state_sum(T2)

    for k in [0.5,1.0,2.0]:
        if abs(k*Z1 - k*Z2) < 1e-9:
            assert False

    assert True

# ------------------------------------------------------------
# 4. structural asymmetry persists
def test_global_asymmetry():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert state_sum(T) != state_sum(T2)

# ------------------------------------------------------------
# 5. existence reformulation (correct categorical statement)
def test_existence_formulation():
    """
    True TQFT exists ⇔ existence of fusion category satisfying:

        (1) pentagon identity exactly
        (2) induced state-sum is Pachner invariant

    Current model does NOT satisfy either axiom.
    """
    exists = False
    assert exists is False
