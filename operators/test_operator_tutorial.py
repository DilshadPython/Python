"""
tests/test_operator_tutorial.py — Unit Tests for Python Operators Tutorial Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comprehensive unit test suite validating all 3 operator titles:
1. Title 1: Arithmetic & Assignment Operators
2. Title 2: Comparison & Logical Operators
3. Title 3: Advanced Operators, Custom Dunders & Range Evolution
"""
import pytest
from cloud_app.tutorials.operator_basics import (
    CustomVector2D,
    PermissionFlags,
    calculate_arithmetic_operations,
    calculate_complex_arithmetic,
    demonstrate_assignment_operators,
    demonstrate_inplace_sequence_mutations,
    evaluate_comparison_and_logical,
    evaluate_chained_range_comparison,
    evaluate_short_circuit_safety,
    perform_bitwise_operations,
    inspect_operator_module_and_dunders,
    inspect_range_operator_features,
    inspect_range_attributes_and_methods,
    demonstrate_all_operators,
)


class TestOperatorTutorial:
    """Master test suite covering all 3 operator titles."""

    # ── TITLE 1 TESTS: ARITHMETIC AND ASSIGNMENT ─────────────────────────────

    def test_arithmetic_operations_success(self):
        res = calculate_arithmetic_operations(10, 2)
        assert res["addition"] == 12
        assert res["subtraction"] == 8
        assert res["multiplication"] == 20
        assert res["float_division"] == 5.0
        assert res["floor_division"] == 5
        assert res["modulus"] == 0
        assert res["exponentiation"] == 100

    def test_complex_arithmetic_operations(self):
        res = calculate_complex_arithmetic(3 + 4j, 1 - 2j)
        assert res["addition"] == 4 + 2j
        assert res["multiplication"] == 11 - 2j

    def test_assignment_and_walrus_operators(self):
        res = demonstrate_assignment_operators(10.0)
        assert res["initial"] == 10.0
        assert res["add_assign"] == 15.0
        assert res["walrus_assign"] == 100.0

    def test_inplace_sequence_mutations(self):
        mutated_list, counts = demonstrate_inplace_sequence_mutations()
        assert len(mutated_list) == 10
        assert counts["apples"] == 15

    # ── TITLE 2 TESTS: COMPARISON AND LOGICAL ────────────────────────────────

    def test_comparison_and_logical(self):
        res = evaluate_comparison_and_logical(10, 5)
        assert res["equal"] is False
        assert res["not_equal"] is True
        assert res["greater_than"] is True

    def test_chained_range_comparison(self):
        assert evaluate_chained_range_comparison(50, 10, 100) is True
        assert evaluate_chained_range_comparison(5, 10, 100) is False

    def test_short_circuit_safety(self):
        possible, val = evaluate_short_circuit_safety([20, 10])
        assert possible is True
        assert val == 5

    def test_bitwise_operations(self):
        res = perform_bitwise_operations(12, 5)
        assert res["bitwise_and"] == 4
        assert res["bitwise_or"] == 13

    # ── TITLE 3 TESTS: ADVANCED DUNDERS AND RANGE ────────────────────────────

    def test_custom_vector_operator_overloading(self):
        v1 = CustomVector2D(3, 4)
        v2 = CustomVector2D(1, 2)
        assert (v1 + v2) == CustomVector2D(4, 6)
        assert (v1 * 3) == CustomVector2D(9, 12)
        assert 3.0 in v1

    def test_permission_flags_overloading(self):
        read_write = PermissionFlags(PermissionFlags.READ) | PermissionFlags(PermissionFlags.WRITE)
        assert PermissionFlags.READ in read_write
        assert PermissionFlags.WRITE in read_write
        assert PermissionFlags.EXEC not in read_write

    def test_operator_module_reflection(self):
        refl = inspect_operator_module_and_dunders()
        assert refl["operator_add"] == 19
        assert refl["top_student"] == "Charlie"

    def test_range_operator_features(self):
        res = inspect_range_operator_features(0, 100, 5)
        assert res["start"] == 0
        assert res["stop"] == 100
        assert res["step"] == 5
        assert res["contains_target"] is True

    def test_inspect_range_attributes_reflection(self):
        refl = inspect_range_attributes_and_methods()
        assert refl["total_attributes_count"] > 10
        assert refl["has_count_method"] is True

    def test_demonstrate_all_operators(self):
        summary = demonstrate_all_operators()
        assert "title_1_arithmetic_assignment" in summary
        assert "title_2_comparison_logical" in summary
        assert "title_3_advanced_dunders_range" in summary
