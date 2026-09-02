# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import unittest: Python standard library unit test framework.
# - from range_reverse_evolution import demonstrate_range_reversing_mechanics, demonstrate_memory_and_dir_introspection
# =========================================================================
import unittest
from range_reverse_evolution import demonstrate_range_reversing_mechanics, demonstrate_memory_and_dir_introspection


class TestRangeEvolution(unittest.TestCase):
    """
    Unit tests for Step 3 Range Evolution and Performance (range reversal, RAM benchmarks, dir() introspection).
    """

    def test_range_reversing_mechanics(self) -> None:
        res = demonstrate_range_reversing_mechanics()
        self.assertEqual(res["negative_step_range"], [10, 8, 6, 4, 2])
        self.assertEqual(res["reversed_range_list"], [10, 8, 6, 4, 2])
        self.assertTrue(res["are_sequences_equal"])

    def test_memory_and_dir_introspection(self) -> None:
        res = demonstrate_memory_and_dir_introspection()
        self.assertTrue(res["is_lazy_memory_constant"])
        self.assertLess(res["lazy_reversed_iter_bytes"], res["materialized_list_slice_bytes"])
        self.assertIn("__iter__", res["dunder_methods_dir_reversed"])
        self.assertIn("__next__", res["dunder_methods_dir_reversed"])
        self.assertIn("python_2_7", res["cpython_evolution"])
        self.assertIn("python_3_13", res["cpython_evolution"])


if __name__ == "__main__":
    unittest.main()
