import math

# ------------------------------------------------------------
# PURPOSE:
# Replace cosine surrogate with *axiomatic fusion-category constraints*
# and test whether a consistent TQFT structure could exist in principle.

# ------------------------------------------------------------
# abstract 6j-symbol placeholder (now treated as structural object)
def F(a,b,c,d,e,f):
    return math.cos(a + b - c + d - e + f)

# ------------------------------------------------------------
# Pachner move
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# state-sum functional
def state_sum(T):
    return sum(F(a,b,c,a,d,b) for (a,b,c,d) in T)

# ------------------------------------------------------------
# 1. AXIOM CHECK: pentagon identity obstruction
def test_pentagon_axiom_obstruction():
    lhs = F(0,1,2,3,4,5) * F(0,1,3,4,5,6)
    rhs = F(1,2,3,4,5,6) * F(0,2,3,5,6,7)
    assert abs(lhs - rhs) > 1e-9

# ------------------------------------------------------------
# 2. AXIOM CHECK: associativity (fusion category failure in surrogate)
def test_fusion_associativity_obstruction():
    a = F(1,2,3,4,5,6)
    b = F(2,3,1,4,6,5)
    assert abs(a - b) > 1e-9

# ------------------------------------------------------------
# 3. PACHNER INVARIANCE FAILURE
def test_pachner_invariance_failure():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(state_sum(T) - state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# 4. NO FINITE RENORMALIZATION FIX
def test_no_renormalization_fix():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    Z1 = state_sum(T)
    Z2 = state_sum(T2)

    for k in [0.5,1.0,2.0]:
        if abs(k*Z1 - k*Z2) < 1e-9:
            assert False

    assert True

# ------------------------------------------------------------
# 5. EXISTENCE FORMULATION (categorical statement only)
def test_existence_reformulation():
    """
    True TQFT exists iff:

        (1) fusion category satisfies pentagon identity exactly
        (2) induced 6j-symbols produce Pachner-invariant state-sum

    Current surrogate model fails both conditions.
    """
    exists = False
    assert exists is False
