from PachnerInvariant.fusion_solver import solve_fusion_category_system


def test_fusion_solver_returns_structured_result():
    result = solve_fusion_category_system()
    assert result.variable_count >= 1
    assert result.pentagon_equation_count >= 1
    assert isinstance(result.solution_count, int)
    assert isinstance(result.has_nontrivial_solution, bool)
