from PachnerInvariant.fusion_category_input import fibonacci_category
from PachnerInvariant.pentagon_constraints import build_pentagon_constraints


def test_pentagon_constraint_system_builds():
    fc = fibonacci_category()
    system = build_pentagon_constraints(fc)
    assert len(system.variables) >= 1
    assert len(system.pentagon_equations) >= 1
