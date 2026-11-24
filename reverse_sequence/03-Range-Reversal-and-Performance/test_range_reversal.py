"""
Unit test suite for Step 3: Range Reversal, Memory Benchmark, & Reflection.
"""
# "import unittest" loads unit testing framework.
import unittest

# "from range_reversal_evolution import ..." imports range reversal functions.
from range_reversal_evolution import (
    reverse_range_with_builtin,
    reverse_range_with_negative_step,
    compare_reversed_range_memory_efficiency,
    inspect_range_attributes_and_methods,
    document_python_version_evolution,
)


class TestRangeReversal(unittest.TestCase):
    """
    Test suite verifying reversed(range), negative step range, memory benchmarks, and dir(range) reflection.
    """

    def test_reverse_range_with_builtin(self) -> None:
        """Verify reversed(range(start, stop, step)) output values."""
        res = reverse_range_with_builtin(0, 10, 2)  # 0, 2, 4, 6, 8 -> 8, 6, 4, 2, 0
        self.assertEqual(res, [8, 6, 4, 2, 0])

    def test_reverse_range_with_negative_step(self) -> None:
        """Verify negative step range() output values."""
        res = reverse_range_with_negative_step(1, 10, 2)  # 9, 7, 5, 3, 1
        self.assertEqual(res, [9, 7, 5, 3, 1])

    def test_compare_reversed_range_memory_efficiency(self) -> None:
        """Verify O(1) RAM footprint for range_iterator object."""
        mem_info = compare_reversed_range_memory_efficiency(1000)
        self.assertTrue(mem_info["is_range_iterator_constant_memory"])
        self.assertLess(mem_info["range_iterator_bytes"], mem_info["materialized_list_bytes"])

    def test_inspect_range_attributes_and_methods(self) -> None:
        """Verify dir(range) introspection matrix returns start, stop, step, index, count, reversed."""
        info = inspect_range_attributes_and_methods()
        self.assertEqual(info["start"], 10)
        self.assertEqual(info["stop"], 100)
        self.assertEqual(info["step"], 5)
        self.assertIn("start", info["public_methods_and_attrs"])
        self.assertIn("stop", info["public_methods_and_attrs"])
        self.assertIn("step", info["public_methods_and_attrs"])
        self.assertIn("count", info["public_methods_and_attrs"])
        self.assertIn("index", info["public_methods_and_attrs"])
        self.assertEqual(info["reversed_range_values"], [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10])

    def test_document_python_version_evolution(self) -> None:
        """Verify version evolution matrix maps all major milestones from 2.7 to 3.13."""
        matrix = document_python_version_evolution()
        self.assertIn("Python 2.7", matrix)
        self.assertIn("Python 3.0-3.4", matrix)
        self.assertIn("Python 3.5-3.8", matrix)
        self.assertIn("Python 3.9-3.11", matrix)
        self.assertIn("Python 3.12-3.13", matrix)


if __name__ == "__main__":
    unittest.main()
