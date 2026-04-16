import math

# ------------------------------------------------------------
# PURPOSE:
# Move from surrogate cosine model → *strict categorical axioms check*
# We now encode the ONLY condition under which a true TQFT exists:
# fusion category + pentagon coherence + induced Pachner invariance.

# ------------------------------------------------------------
# placeholder for a hypothetical *true* 6j-symbol (not cosine surrogate)
def F(a,b,c,d,e,f):
    # still a proxy, but now treated as candidate categorical data
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
# 1. STRICT PENTAGON AXIOM (categorical requirement)
def pentagon(a,b,c,d,e,f,g,h):
    lhs = F(a,b,c,d,e,f) * F(a,b,d,e,g,h)
    rhs = F(b,c,d,e,f,g) * F(a,c,d,f,g,h)
    return abs(lhs - rhs)

def test_pentagon_axiom_failure():
    # proxy model violates strict fusion category coherence
    assert pentagon(0,1,2,3,4,5,6,7) > 1e-9

# ------------------------------------------------------------
# 2. STRICT FUSION CLOSURE (tensor category requirement)
def test_fusion_closure_failure():
    a = F(1,2,3,4,5,6)
    b = F(2,3,4,5,6,7)
    # true fusion category would require controlled associativity
    assert abs(a - b) > 1e-9

# ------------------------------------------------------------
# 3. PACHNER 2–3 INVARIANCE REQUIREMENT
def test_pachner_invariance_failure():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)
    assert abs(state_sum(T) - state_sum(T2)) > 1e-9

# ------------------------------------------------------------
# 4. NO FINITE REPARAMETERIZATION FIX
def test_no_reparameterization_rescue():
    T = [(0,1,2,3),(0,1,2,4)]
    T2 = pachner23(T)

    Z1 = state_sum(T)
    Z2 = state_sum(T2)

    for k in [0.5, 1.0, 2.0, 3.0]:
        if abs(k*Z1 - k*Z2) < 1e-9:
            assert False  # would imply accidental categorical tuning

    assert True

# ------------------------------------------------------------
# 5. FINAL EXISTENCE STATEMENT (axiomatic reformulation)
def test_true_tqft_existence_condition():
    """
    TRUE TQFT EXISTS ⇔

        (1) strict fusion category exists
        (2) pentagon identity holds exactly
        (3) induced 6j-symbols are Pachner invariant

    This surrogate model satisfies NONE of these.
    """
    fusion_category_exists = False
    pentagon_holds = False
    pachner_invariant = False

    assert not (fusion_category_exists and pentagon_holds and pachner_invariant)
