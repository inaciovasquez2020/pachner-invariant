from PachnerInvariant.fusion_category_input import fibonacci_category
from PachnerInvariant.pachner23_categorical import default_pachner23_instance
from PachnerInvariant.pentagon_constraints import build_f_symbols


def test_default_pachner23_instance_uses_f_symbols():
    fc = fibonacci_category()
    f_symbols = build_f_symbols(fc)
    instance = default_pachner23_instance(fc)
    assert instance.left_keys[0] in f_symbols
    assert instance.right_keys[0] in f_symbols
