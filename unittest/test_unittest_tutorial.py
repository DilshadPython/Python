"""
tests/test_unittest_tutorial.py — Unit Tests for Unittest Tutorial Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comprehensive test suite validating functions, classes, range integration,
and reflection matrix in cloud_app.tutorials.unittest_basics.
"""
import math
import sys
import unittest
import pytest

from cloud_app.tutorials.unittest_basics import (
    add_numbers,
    divide_numbers,
    calculate_circle_area,
    format_welcome_message,
    StudentProfile,
    BasicAssertionsTestCase,
    StudentFixtureTestCase,
    inspect_range_properties,
    inspect_testcase_reflection,
    demonstrate_basic_unittest_assertions,
    demonstrate_fixtures_and_subtests,
    demonstrate_range_integration,
    demonstrate_reflection_matrix,
)


class TestUnittestTutorial:
    """Master test suite verifying all functions and entities in unittest_basics."""

    def test_add_numbers_success(self):
        assert add_numbers(10, 20) == 30
        assert add_numbers(-5, 5) == 0
        assert add_numbers(2.5, 3.5) == 6.0

    def test_add_numbers_invalid_types(self):
        with pytest.raises(TypeError):
            add_numbers("10", 20)
        with pytest.raises(TypeError):
            add_numbers(True, 5)

    def test_divide_numbers_success(self):
        assert divide_numbers(100, 4) == 25.0
        assert divide_numbers(7, 2) == 3.5

    def test_divide_numbers_zero_division(self):
        with pytest.raises(ValueError) as exc_info:
            divide_numbers(10, 0)
        assert "cannot be zero" in str(exc_info.value)

    def test_divide_numbers_invalid_types(self):
        with pytest.raises(TypeError):
            divide_numbers(10, "2")

    def test_calculate_circle_area_success(self):
        assert math.isclose(calculate_circle_area(1.0), math.pi, rel_tol=1e-5)
        assert math.isclose(calculate_circle_area(5.0), 78.5398163, rel_tol=1e-5)

    def test_calculate_circle_area_negative_radius(self):
        with pytest.raises(ValueError) as exc_info:
            calculate_circle_area(-5.0)
        assert "cannot be negative" in str(exc_info.value)

    def test_calculate_circle_area_invalid_types(self):
        with pytest.raises(TypeError):
            calculate_circle_area(True)
        with pytest.raises(TypeError):
            calculate_circle_area("5")

    def test_format_welcome_message(self):
        assert format_welcome_message("Guido") == "Welcome back, Guido!"
        assert format_welcome_message("") == "Welcome back, Guest!"
        assert format_welcome_message(None) == "Welcome back, Guest!"

    def test_student_profile_success(self):
        student = StudentProfile("Ada", "Lovelace", 2000.0)
        assert student.full_name == "Ada Lovelace"
        assert student.email == "ada.lovelace@university.edu"
        assert student.tuition_balance == 2000.0

    def test_student_profile_discount(self):
        student = StudentProfile("Grace", "Hopper", 1000.0)
        updated = student.apply_loan_discount(0.90)
        assert updated == 900.0
        assert student.tuition_balance == 900.0

    def test_student_profile_invalid_inputs(self):
        with pytest.raises(ValueError):
            StudentProfile("", "Lovelace", 1000.0)
        with pytest.raises(ValueError):
            StudentProfile("Ada", "Lovelace", -500.0)

    def test_inspect_range_properties(self):
        r = range(0, 100, 5)
        info = inspect_range_properties(r)
        assert info["start"] == 0
        assert info["stop"] == 100
        assert info["step"] == 5
        assert info["length"] == 20
        assert info["memory_bytes"] < 100
        assert info["contains_start"] is True

    def test_inspect_range_properties_invalid_type(self):
        with pytest.raises(TypeError):
            inspect_range_properties([0, 1, 2])

    def test_inspect_testcase_reflection(self):
        info = inspect_testcase_reflection()
        assert info["assertion_methods_count"] >= 10
        assert "assertEqual" in info["assertion_methods"]
        assert "testcase_instance_properties" in info
        assert "id" in info["testcase_instance_properties"]
        assert info["has_subtest"] is True

    def test_demonstrate_functions(self):
        basic_res = demonstrate_basic_unittest_assertions()
        assert isinstance(basic_res, dict)
        assert basic_res["add_numbers(15, 25)"] == 40

        runner_res = demonstrate_fixtures_and_subtests()
        assert isinstance(runner_res, dict)
        assert runner_res["was_successful"] is True

        range_res = demonstrate_range_integration()
        assert isinstance(range_res, dict)
        assert range_res["is_constant_memory"] is True

        refl_res = demonstrate_reflection_matrix()
        assert isinstance(refl_res, dict)
        assert refl_res["has_subtest"] is True
