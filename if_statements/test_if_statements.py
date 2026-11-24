"""Unit Testing Suite for Python Conditional Statements ('If-Statement' Module).

This module contains exhaustive unit tests using Python's standard 'unittest' framework
to validate all conditional functions, branching logic, edge cases, exception handling,
and version-agnostic features across the entire 'If-Statement' learning suite.

Import Notes:
    - 'import unittest': The standard Python unit testing framework for test suites,
      fixtures, and assertion methods.
    - 'import sys': Used to dynamically configure import search paths and check Python runtime.
    - 'import importlib': Used to safely import modules whose names are Python reserved keywords
      (such as 'if.py' and 'elif.py').
"""

import sys
import os
import importlib
import unittest

# Ensure the 'If-Statement' directory is included in sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# Safe imports for modules with standard valid identifiers
import advance_if
import check_number
import if_1
import if_2
import if_3
import if_advance
import if_and
import if_elif
import if_else
import if_else_1
import if_for
import if_is
import if_nesting
import if_not
import if_options
import if_or
import if_then
import if_what
import match
import more_if
import not_match
import triangle

# Dynamic imports for keyword-named modules ('if.py' and 'elif.py')
mod_if = importlib.import_module("if")
mod_elif = importlib.import_module("elif")


class TestAdvanceIf(unittest.TestCase):
    """Test ternary conditional expressions in advance_if.py."""

    def test_get_minimum_value(self):
        self.assertEqual(advance_if.get_minimum_value(50, 25), 25)
        self.assertEqual(advance_if.get_minimum_value(10, 100), 10)
        self.assertEqual(advance_if.get_minimum_value(-5, -20), -20)

    def test_classify_number_ternary(self):
        self.assertEqual(advance_if.classify_number_ternary(15), "Positive")
        self.assertEqual(advance_if.classify_number_ternary(-8), "Negative")
        self.assertEqual(advance_if.classify_number_ternary(0), "Zero")

    def test_demo_advance_if(self):
        min_val, classification = advance_if.demo_advance_if()
        self.assertEqual(min_val, 25)
        self.assertEqual(classification, "Negative")


class TestCheckNumber(unittest.TestCase):
    """Test number classification and parity in check_number.py."""

    def test_classify_number_sign(self):
        self.assertEqual(check_number.classify_number_sign(10), "Positive")
        self.assertEqual(check_number.classify_number_sign(-5), "Negative")
        self.assertEqual(check_number.classify_number_sign(0), "Zero")

    def test_check_parity(self):
        self.assertEqual(check_number.check_parity(4), "Even")
        self.assertEqual(check_number.check_parity(7), "Odd")

    def test_analyze_number(self):
        res = check_number.analyze_number(42)
        self.assertEqual(res, {"sign": "Positive", "parity": "Even"})


class TestElifModule(unittest.TestCase):
    """Test multi-branch grading and temperature logic in elif.py."""

    def test_evaluate_grade(self):
        self.assertEqual(mod_elif.evaluate_grade(95), "Grade A (Excellent)")
        self.assertEqual(mod_elif.evaluate_grade(85), "Grade B (Good)")
        self.assertEqual(mod_elif.evaluate_grade(75), "Grade C (Satisfactory)")
        self.assertEqual(mod_elif.evaluate_grade(65), "Grade D (Pass)")
        self.assertEqual(mod_elif.evaluate_grade(50), "Grade F (Fail)")

    def test_evaluate_grade_exceptions(self):
        with self.assertRaises(ValueError):
            mod_elif.evaluate_grade(-10)
        with self.assertRaises(ValueError):
            mod_elif.evaluate_grade(105)

    def test_classify_temperature(self):
        self.assertEqual(mod_elif.classify_temperature(40), "Extreme Heat")
        self.assertEqual(mod_elif.classify_temperature(28), "Warm / Summer")
        self.assertEqual(mod_elif.classify_temperature(20), "Mild / Pleasant")
        self.assertEqual(mod_elif.classify_temperature(2), "Cold / Freezing Point")
        self.assertEqual(mod_elif.classify_temperature(-10), "Sub-Zero / Below Freezing")


class TestIfBasic(unittest.TestCase):
    """Test weekday classification in if.py."""

    def test_classify_day_type(self):
        self.assertIn("Weekend", mod_if.classify_day_type("Saturday"))
        self.assertIn("Weekend", mod_if.classify_day_type("Sunday"))
        self.assertIn("Workday", mod_if.classify_day_type("Monday"))
        self.assertIn("Workday", mod_if.classify_day_type("Thursday"))


class TestIf1(unittest.TestCase):
    """Test numeric magnitude comparisons in if_1.py."""

    def test_compare_numbers(self):
        self.assertIn("strictly lower", if_1.compare_numbers(23, 30))
        self.assertIn("strictly greater", if_1.compare_numbers(50, 30))
        self.assertIn("equal", if_1.compare_numbers(30, 30))


class TestIf2(unittest.TestCase):
    """Test string equality comparison in if_2.py."""

    def test_verify_string_match(self):
        self.assertTrue(if_2.verify_string_match("Hello", "Hello"))
        self.assertFalse(if_2.verify_string_match("Hello", "World"))


class TestIf3(unittest.TestCase):
    """Test integer value equality in if_3.py."""

    def test_check_integer_equality(self):
        self.assertTrue(if_3.check_integer_equality(100, 100))
        self.assertFalse(if_3.check_integer_equality(100, 200))


class TestIfAdvance(unittest.TestCase):
    """Test compound logical expressions in if_advance.py."""

    def test_evaluate_compound_conditions(self):
        res = if_advance.evaluate_compound_conditions(100, 100, 300)
        self.assertTrue(res["all_conditions_true"])
        self.assertTrue(res["at_least_one_true"])
        self.assertTrue(res["negated_check"])


class TestIfAnd(unittest.TestCase):
    """Test logical AND permissions in if_and.py."""

    def test_verify_user_access(self):
        self.assertTrue(if_and.verify_user_access("Student", True))
        self.assertFalse(if_and.verify_user_access("Student", False))
        self.assertFalse(if_and.verify_user_access("Guest", True))


class TestIfElif(unittest.TestCase):
    """Test age stage categorization in if_elif.py."""

    def test_categorize_age_stage(self):
        self.assertEqual(if_elif.categorize_age_stage(10), "Minor")
        self.assertEqual(if_elif.categorize_age_stage(25), "Adult")
        self.assertEqual(if_elif.categorize_age_stage(70), "Senior")

    def test_categorize_age_negative_exception(self):
        with self.assertRaises(ValueError):
            if_elif.categorize_age_stage(-1)


class TestIfElse(unittest.TestCase):
    """Test technology string matching in if_else.py."""

    def test_verify_technology(self):
        self.assertTrue(if_else.verify_technology("Hello Python"))
        self.assertFalse(if_else.verify_technology("Java"))


class TestIfElse1(unittest.TestCase):
    """Test password strength validation in if_else_1.py."""

    def test_validate_password_strength(self):
        self.assertIn("Strong Password", if_else_1.validate_password_strength("SecureP@ss2026"))
        self.assertIn("Weak Password", if_else_1.validate_password_strength("secret"))


class TestIfFor(unittest.TestCase):
    """Test loop iteration filtering in if_for.py."""

    def test_filter_numbers_above_threshold(self):
        above, below = if_for.filter_numbers_above_threshold(5, 10)
        self.assertEqual(above, [6, 7, 8, 9])
        self.assertEqual(below, [0, 1, 2, 3, 4, 5])


class TestIfIs(unittest.TestCase):
    """Test identity vs equality comparison in if_is.py."""

    def test_compare_value_and_identity(self):
        list_a = [1, 2, 3]
        list_b = [1, 2, 3]
        res = if_is.compare_value_and_identity(list_a, list_b)
        self.assertTrue(res["value_equal"])
        self.assertFalse(res["identity_same"])

        list_c = list_a
        res_alias = if_is.compare_value_and_identity(list_a, list_c)
        self.assertTrue(res_alias["identity_same"])


class TestIfNesting(unittest.TestCase):
    """Test nested vs flat conditional structures in if_nesting.py."""

    def test_evaluate_housing_option(self):
        self.assertIn("spacious private garden", if_nesting.evaluate_housing_option("apartment", "house"))
        self.assertIn("flat without a garden", if_nesting.evaluate_housing_option("apartment", "commercial"))
        self.assertEqual(if_nesting.evaluate_housing_option("villa", "house"), "Unknown housing category.")

    def test_evaluate_housing_flat(self):
        self.assertIn("spacious private garden", if_nesting.evaluate_housing_flat("apartment", "house"))
        self.assertIn("flat without a garden", if_nesting.evaluate_housing_flat("apartment", "commercial"))
        self.assertEqual(if_nesting.evaluate_housing_flat("villa", "house"), "Unknown housing category.")


class TestIfNot(unittest.TestCase):
    """Test logical NOT inversion in if_not.py."""

    def test_check_registration_status(self):
        self.assertIn("IS registered", if_not.check_registration_status(True))
        self.assertIn("NOT registered", if_not.check_registration_status(False))


class TestIfOptions(unittest.TestCase):
    """Test truthiness evaluation in if_options.py."""

    def test_evaluate_truthiness(self):
        self.assertFalse(if_options.evaluate_truthiness(False))
        self.assertFalse(if_options.evaluate_truthiness(None))
        self.assertFalse(if_options.evaluate_truthiness(0))
        self.assertFalse(if_options.evaluate_truthiness([]))
        self.assertTrue(if_options.evaluate_truthiness("Hello"))
        self.assertTrue(if_options.evaluate_truthiness([1, 2]))

    def test_get_falsy_examples(self):
        falsy_dict = if_options.get_falsy_examples()
        for key, val in falsy_dict.items():
            self.assertFalse(bool(val), f"{key} should evaluate to Falsy")


class TestIfOr(unittest.TestCase):
    """Test logical OR permissions in if_or.py."""

    def test_verify_any_permission(self):
        self.assertTrue(if_or.verify_any_permission("Student", False))
        self.assertTrue(if_or.verify_any_permission("Guest", True))
        self.assertFalse(if_or.verify_any_permission("Guest", False))


class TestIfThen(unittest.TestCase):
    """Test divisibility and parity evaluation in if_then.py."""

    def test_evaluate_number_properties(self):
        self.assertIn("divisible by both 3 and 5", if_then.evaluate_number_properties(15))
        self.assertIn("Even number", if_then.evaluate_number_properties(4))
        self.assertIn("Odd number", if_then.evaluate_number_properties(7))


class TestIfWhat(unittest.TestCase):
    """Test literal boolean evaluation in if_what.py."""

    def test_evaluate_literal_condition(self):
        self.assertIn("True", if_what.evaluate_literal_condition(True))
        self.assertIn("False", if_what.evaluate_literal_condition(False))


class TestMatch(unittest.TestCase):
    """Test pattern matching in match.py."""

    def test_match_team_country(self):
        self.assertEqual(match.match_team_country("Manchester"), "English Premier League Team")
        self.assertEqual(match.match_team_country("Real Madrid"), "Spanish La Liga Team")
        self.assertEqual(match.match_team_country("Unknown FC"), "Uncategorized Team")


class TestMoreIf(unittest.TestCase):
    """Test dynamic registration truthiness in more_if.py."""

    def test_is_user_registered(self):
        self.assertTrue(more_if.is_user_registered(["Alice"]))
        self.assertTrue(more_if.is_user_registered(1))
        self.assertFalse(more_if.is_user_registered([]))
        self.assertFalse(more_if.is_user_registered(None))


class TestNotMatch(unittest.TestCase):
    """Test fallback pattern matching wildcard in not_match.py."""

    def test_classify_team_with_fallback(self):
        self.assertEqual(not_match.classify_team_with_fallback("Real Madrid"), "Spanish Team")
        self.assertIn("does not exist", not_match.classify_team_with_fallback("Unknown FC"))


class TestTriangle(unittest.TestCase):
    """Test triangle validation and classification in triangle.py."""

    def test_is_valid_triangle(self):
        self.assertTrue(triangle.is_valid_triangle(3, 4, 5))
        self.assertTrue(triangle.is_valid_triangle(5, 5, 5))
        self.assertFalse(triangle.is_valid_triangle(1, 2, 3))
        self.assertFalse(triangle.is_valid_triangle(-1, 4, 5))

    def test_classify_triangle(self):
        self.assertEqual(triangle.classify_triangle(5, 5, 5), "Equilateral Triangle")
        self.assertEqual(triangle.classify_triangle(5, 5, 8), "Isosceles Triangle")
        self.assertEqual(triangle.classify_triangle(3, 4, 5), "Scalene Triangle")

    def test_classify_triangle_invalid_exception(self):
        with self.assertRaises(ValueError):
            triangle.classify_triangle(1, 2, 10)


if __name__ == "__main__":
    unittest.main()
