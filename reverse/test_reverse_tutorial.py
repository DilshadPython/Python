# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import unittest: Standard library testing framework.
# - from reverse_sequence_basics import (
#       demonstrate_01_fundamentals_basics, demonstrate_01_fundamentals_slicing,
#       demonstrate_02_advanced_custom_reverse, demonstrate_02_advanced_dict_and_matrix_reversing,
#       demonstrate_03_range_evolution_and_performance, run_all_reverse_module_demos
#   )
# =========================================================================
import unittest
from reverse_sequence_basics import (
    demonstrate_01_fundamentals_basics,
    demonstrate_01_fundamentals_slicing,
    demonstrate_02_advanced_custom_reverse,
    demonstrate_02_advanced_dict_and_matrix_reversing,
    demonstrate_03_range_evolution_and_performance,
    run_all_reverse_module_demos,
)


class TestReverseSequenceMaster(unittest.TestCase):
    """
    Master unit test suite executing all curriculum steps for Reverse Sequence tutorial.
    """

    def test_01_fundamentals_basics(self) -> None:
        res = demonstrate_01_fundamentals_basics([1, 2, 3], ("a", "b"), "test")
        self.assertEqual(res["reversed_list"], [3, 2, 1])
        self.assertEqual(res["reversed_tuple"], ("b", "a"))
        self.assertEqual(res["reversed_str"], "tset")
        self.assertEqual(res["inplace_mutated_list"], [3, 2, 1])
        self.assertIsNone(res["inplace_return_val"])

    def test_01_fundamentals_slicing(self) -> None:
        res = demonstrate_01_fundamentals_slicing([10, 20, 30], "python")
        self.assertEqual(res["sliced_list"], [30, 20, 10])
        self.assertEqual(res["sliced_str"], "nohtyp")
        self.assertTrue(res["set_type_error_caught"])

    def test_02_advanced_custom_reverse(self) -> None:
        res = demonstrate_02_advanced_custom_reverse()
        self.assertEqual(res["forward_items"], [1, 2, 3, 4])
        self.assertEqual(res["custom_reversed_items"], [40, 30, 20, 10])

    def test_02_advanced_dict_and_matrix_reversing(self) -> None:
        res = demonstrate_02_advanced_dict_and_matrix_reversing({"a": 1, "b": 2}, [[1, 2], [3, 4]])
        self.assertEqual(res["reversed_keys"], ["b", "a"])
        self.assertEqual(res["reversed_values"], [2, 1])
        self.assertEqual(res["row_reversed_matrix"], [[3, 4], [1, 2]])
        self.assertEqual(res["col_reversed_matrix"], [[2, 1], [4, 3]])
        self.assertEqual(res["rotated_180_matrix"], [[4, 3], [2, 1]])

    def test_03_range_evolution_and_performance(self) -> None:
        res = demonstrate_03_range_evolution_and_performance()
        self.assertEqual(res["negative_step_range"], [10, 8, 6, 4, 2])
        self.assertEqual(res["reversed_range_list"], [10, 8, 6, 4, 2])
        self.assertTrue(res["are_equal"])
        self.assertTrue(res["is_constant_memory"])
        self.assertIn("__iter__", res["dunder_methods"])
        self.assertIn("python_3_13", res["cpython_evolution"])

    def test_run_all_reverse_module_demos(self) -> None:
        res = run_all_reverse_module_demos()
        self.assertIn("01_fundamentals", res)
        self.assertIn("02_advanced_math", res)
        self.assertIn("03_range_and_performance", res)


if __name__ == "__main__":
    unittest.main()
