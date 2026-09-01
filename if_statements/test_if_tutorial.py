import unittest
from cloud_app.tutorials.if_basics import (
    starter_if_examples,
    logical_operators_and_short_circuit,
    truthiness_and_falsiness_evaluator,
    advanced_ternary_and_identity_checks,
    pattern_matching_and_geometry,
    methods_and_attributes_in_conditionals
)


class TestIfTutorial(unittest.TestCase):
    """Unit test suite for Python If-Statement tutorial module."""

    def test_starter_if_examples(self):
        res = starter_if_examples()
        self.assertTrue(res["is_warm"])
        self.assertTrue(res["access_granted"])
        self.assertEqual(res["assigned_grade"], "B")
        self.assertEqual(res["number_sign"], "Negative")

    def test_logical_operators_and_short_circuit(self):
        res = logical_operators_and_short_circuit()
        self.assertTrue(res["can_drive"])
        self.assertTrue(res["is_special_case"])
        self.assertTrue(res["is_clean_record"])
        self.assertTrue(res["is_eligible"])
        # In 'A and B' where A is False, B is short-circuited (only 'first' evaluated)
        self.assertEqual(res["short_circuit_eval_tracker"], ["first", "or_first"])
        self.assertFalse(res["and_result"])
        self.assertTrue(res["or_result"])

    def test_truthiness_and_falsiness_evaluator_truthy(self):
        res = truthiness_and_falsiness_evaluator([1, 2, 3])
        self.assertTrue(res["is_truthy"])
        self.assertEqual(res["category"], "Truthy Object")

    def test_truthiness_and_falsiness_evaluator_falsy(self):
        res_none = truthiness_and_falsiness_evaluator(None)
        self.assertFalse(res_none["is_truthy"])
        self.assertEqual(res_none["category"], "NoneType (Falsy)")

        res_empty_list = truthiness_and_falsiness_evaluator([])
        self.assertFalse(res_empty_list["is_truthy"])
        self.assertEqual(res_empty_list["category"], "Empty Container (Falsy)")

        res_zero = truthiness_and_falsiness_evaluator(0)
        self.assertFalse(res_zero["is_truthy"])
        self.assertEqual(res_zero["category"], "Zero/Empty Primitive (Falsy)")

    def test_advanced_ternary_and_identity_checks(self):
        res = advanced_ternary_and_identity_checks("Developer", sentinel=None)
        self.assertEqual(res["ternary_status"], "Active")
        self.assertTrue(res["value_equality_check"])
        self.assertFalse(res["identity_check_different_objs"])
        self.assertTrue(res["identity_check_same_ref"])
        self.assertTrue(res["is_sentinel_none"])

    def test_pattern_matching_and_geometry_valid(self):
        res_equilateral = pattern_matching_and_geometry((5, 5, 5), "start")
        self.assertTrue(res_equilateral["is_valid_triangle"])
        self.assertEqual(res_equilateral["triangle_type"], "Equilateral")
        self.assertEqual(res_equilateral["action_result"], "System Initialized")

        res_isosceles = pattern_matching_and_geometry((5, 5, 8), "stop")
        self.assertTrue(res_isosceles["is_valid_triangle"])
        self.assertEqual(res_isosceles["triangle_type"], "Isosceles")
        self.assertEqual(res_isosceles["action_result"], "System Suspended")

        res_scalene = pattern_matching_and_geometry((3, 4, 5), "status")
        self.assertTrue(res_scalene["is_valid_triangle"])
        self.assertEqual(res_scalene["triangle_type"], "Scalene")

    def test_pattern_matching_and_geometry_invalid_triangle(self):
        res_invalid = pattern_matching_and_geometry((1, 2, 10), "unknown_cmd")
        self.assertFalse(res_invalid["is_valid_triangle"])
        self.assertEqual(res_invalid["triangle_type"], "Invalid Triangle")
        self.assertEqual(res_invalid["action_result"], "Fallback Action for 'unknown_cmd'")

    def test_pattern_matching_and_geometry_invalid_types(self):
        with self.assertRaises(TypeError):
            pattern_matching_and_geometry("invalid_sides", "start")
        with self.assertRaises(TypeError):
            pattern_matching_and_geometry((3, 4, 5), 12345)

    def test_methods_and_attributes_in_conditionals(self):
        res = methods_and_attributes_in_conditionals([1, 2, 3], "12345", [2, 4, 6])
        self.assertTrue(res["has_len_attribute"])
        self.assertFalse(res["is_function_callable"])
        self.assertFalse(res["is_string_type"])
        self.assertTrue(res["is_numeric_text"])
        self.assertFalse(res["starts_with_prefix"])
        self.assertTrue(res["all_positive"])
        self.assertTrue(res["has_even"])
        self.assertTrue(res["is_modern_python"])


if __name__ == "__main__":
    unittest.main()
