"""
tests/test_operator_tutorial.py — Unit Tests for Python Operators Tutorial Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comprehensive unit test suite validating arithmetic, assignment, comparison,
logical, bitwise, walrus (:=), range sequence operators, custom operator overloading,
and standard library operator module reflection.
"""
import pytest
import sys
from cloud_app.tutorials.operator_basics import (
    CustomVector2D,
    calculate_arithmetic_operations,
    demonstrate_assignment_operators,
    evaluate_comparison_and_logical,
    perform_bitwise_operations,
    inspect_operator_module_and_dunders,
    inspect_range_operator_features,
    inspect_range_attributes_and_methods,
    demonstrate_all_operators,
)


class TestOperatorTutorial:
    """Master test suite for operator_basics module functions and classes."""

    def test_custom_vector_operator_overloading(self):
        v1 = CustomVector2D(3, 4)
        v2 = CustomVector2D(1, 2)

        # Vector addition (__add__)
        v_sum = v1 + v2
        assert v_sum == CustomVector2D(4, 6)

        # Vector subtraction (__sub__)
        v_sub = v1 - v2
        assert v_sub == CustomVector2D(2, 2)

        # Scalar multiplication (__mul__)
        v_scaled = v1 * 3
        assert v_scaled == CustomVector2D(9, 12)

        # Vector equality (__eq__)
        assert v1 != v2
        assert v1 == CustomVector2D(3, 4)

        # Vector containment (__contains__)
        assert 3.0 in v1
        assert 99.0 not in v1
        assert len(v1) == 2

    def test_custom_vector_invalid_types(self):
        with pytest.raises(TypeError):
            CustomVector2D("3", 4)
        with pytest.raises(TypeError):
            CustomVector2D(3, True)

    def test_operator_module_reflection(self):
        refl = inspect_operator_module_and_dunders()
        assert refl["operator_add"] == 19
        assert refl["operator_sub"] == 11
        assert refl["operator_mul"] == 60
        assert refl["operator_eq"] is False
        assert refl["operator_contains"] is True
        assert refl["top_student"] == "Charlie"
        assert "__add__" in refl["sample_int_dunders"]

    def test_arithmetic_operations_success(self):
        res = calculate_arithmetic_operations(10, 2)
        assert res["addition"] == 12
        assert res["subtraction"] == 8
        assert res["multiplication"] == 20
        assert res["float_division"] == 5.0
        assert res["floor_division"] == 5
        assert res["modulus"] == 0
        assert res["exponentiation"] == 100

    def test_arithmetic_operations_zero_division(self):
        with pytest.raises(ZeroDivisionError) as exc_info:
            calculate_arithmetic_operations(10, 0)
        assert "cannot be zero" in str(exc_info.value)

    def test_arithmetic_operations_invalid_types(self):
        with pytest.raises(TypeError):
            calculate_arithmetic_operations("10", 2)
        with pytest.raises(TypeError):
            calculate_arithmetic_operations(True, 5)

    def test_assignment_and_walrus_operators(self):
        res = demonstrate_assignment_operators(10.0)
        assert res["initial"] == 10.0
        assert res["add_assign"] == 15.0
        assert res["sub_assign"] == 12.0
        assert res["mul_assign"] == 24.0
        assert res["div_assign"] == 6.0
        assert res["floor_div_assign"] == 3.0
        assert res["mod_assign"] == 1.0
        assert res["pow_assign"] == 1.0
        assert res["walrus_assign"] == 100.0

    def test_comparison_and_logical(self):
        res = evaluate_comparison_and_logical(10, 5)
        assert res["equal"] is False
        assert res["not_equal"] is True
        assert res["greater_than"] is True
        assert res["less_than"] is False
        assert res["logical_and"] is True
        assert res["logical_or"] is True
        assert res["logical_not"] is True

    def test_bitwise_operations(self):
        res = perform_bitwise_operations(12, 5)
        assert res["bitwise_and"] == 4
        assert res["bitwise_or"] == 13
        assert res["bitwise_xor"] == 9
        assert res["bitwise_not_a"] == -13
        assert res["left_shift"] == 48
        assert res["right_shift"] == 6

    def test_range_operator_features(self):
        res = inspect_range_operator_features(0, 100, 5)
        assert res["start"] == 0
        assert res["stop"] == 100
        assert res["step"] == 5
        assert res["length"] == 20
        assert res["contains_target"] is True
        assert res["first_element"] == 0
        assert res["memory_bytes"] < 100

    def test_range_operator_invalid_inputs(self):
        with pytest.raises(TypeError):
            inspect_range_operator_features("0", 100, 5)
        with pytest.raises(ValueError):
            inspect_range_operator_features(0, 100, 0)

    def test_inspect_range_attributes_reflection(self):
        refl = inspect_range_attributes_and_methods()
        assert refl["total_attributes_count"] > 10
        assert refl["has_count_method"] is True
        assert refl["has_index_method"] is True

    def test_demonstrate_all_operators(self):
        summary = demonstrate_all_operators()
        assert isinstance(summary, dict)
        assert "arithmetic" in summary
        assert "vector_overloading" in summary
        assert "operator_module_reflection" in summary
