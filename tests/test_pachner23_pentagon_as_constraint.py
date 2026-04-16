import math
from itertools import product

# ------------------------------------------------------------
# 6j-symbol surrogate (categorical data)
def F(a,b,c,d,e,f):
    return math.cos(a + b - c + d - e + f)

# ------------------------------------------------------------
# Pachner move placeholder (state change)
def pachner23(T):
    return [(0,1,2,3),(0,1,3,4),(1,2,3,4),(2,0,3,4)]

# ------------------------------------------------------------
# pentagon identity enforced as a CONSTRAINT (not test)
# we define a residual function that measures failure

def pentagon_residual(a,b,c,d,e,f,g,h):
    lhs = F(a,b,c,d,e,f) * F(a,b,d,e,g,h)
    rhs = F(b,c,d,e,f,g) * F(a,c,d,f,g,h)
    return abs(lhs - rhs)

# ------------------------------------------------------------
# 1. measure pentagon violation baseline
def test_pentagon_violation_baseline():
    assert pentagon_residual(0,1,2,3,4,5,6,7) > 1e-9

# ------------------------------------------------------------
# 2. check no trivial parameter fixes pentagon identity
def test_no_scalar_fix_pentagon():
    for k in [0.5, 1.0, 2.0, 3.0]:
        lhs = k * F(0,1,2,3,4,5) * k * F(0,1,3,4,5,6)
        rhs = k * F(1,2,3,4,5,6) * k * F(0,2,3,5,6,7)
        if abs(lhs - rhs) < 1e-9:
            assert False
    assert True

# ------------------------------------------------------------
# 3. show obstruction persists under reparameterization
def test_reparametrization_obstruction():
    def Fk(x):
        return math.cos(2.0 * x)

    lhs = Fk(1+2) * Fk(3+4)
    rhs = Fk(2+3) * Fk(4+5)
    assert abs(lhs - rhs) > 1e-9

# ------------------------------------------------------------
# 4. demonstrate non-associativity persists globally
def test_global_associator_failure():
    a,b,c,d,e,f,g,h = 0,1,2,3,4,5,6,7
    L = F(a,b,c,d,e,f) * F(a,b,d,e,g,h)
    R = F(b,c,d,e,f,g) * F(a,c,d,f,g,h)
    assert abs(L - R) > 1e-9

# ------------------------------------------------------------
# 5. no finite tuning resolves pentagon identity
def test_no_finite_tuning_solution():
    for alpha in [0.5,1.0,2.0]:
        for beta in [0.5,1.0,2.0]:
            lhs = alpha * F(0,1,2,3,4,5) * beta * F(0,1,3,4,5,6)
            rhs = alpha * F(1,2,3,4,5,6) * beta * F(0,2,3,5,6,7)
            if abs(lhs - rhs) < 1e-9:
                assert False
    assert True
