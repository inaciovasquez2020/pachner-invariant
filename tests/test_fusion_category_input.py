from PachnerInvariant.fusion_category_input import fibonacci_category, all_fs_keys


def test_fibonacci_category_has_simples_and_keys():
    fc = fibonacci_category()
    assert fc.unit == "1"
    assert "tau" in fc.simples
    keys = all_fs_keys(fc)
    assert isinstance(keys, list)
