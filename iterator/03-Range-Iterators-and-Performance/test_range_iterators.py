"""
Unit test suite for Step 3: Range Iterator Performance & Reflection.
"""
# "import unittest" loads unit testing framework.
import unittest

# "from range_iterator_performance import ..." imports range iterator performance functions.
from range_iterator_performance import (
    iterate_range_sequence,
    compare_range_iterator_memory_efficiency,
    inspect_range_attributes_and_methods,
    document_python_version_evolution,
)


class TestRangeIterators(unittest.TestCase):
    """
    Test suite verifying iter(range(n)), memory benchmarks, dir(range) reflection, and version matrix.
    """

    def test_iterate_range_sequence(self) -> None:
        """Verify iter(range(start, stop, step)) yields correct sequence."""
        res = iterate_range_sequence(1, 10, 2)
        self.assertEqual(res, [1, 3, 5, 7, 9])

    def test_compare_range_iterator_memory_efficiency(self) -> None:
        """Verify O(1) RAM footprint for range_iterator object relative to list."""
        mem_info = compare_range_iterator_memory_efficiency(1000)
        self.assertTrue(mem_info["is_range_iterator_constant_memory"])
        self.assertLess(mem_info["range_iterator_bytes"], mem_info["list_bytes"])

    def test_inspect_range_attributes_and_methods(self) -> None:
        """Verify dir(range) introspection matrix returns start, stop, step, index, count."""
        info = inspect_range_attributes_and_methods()
        self.assertEqual(info["start"], 10)
        self.assertEqual(info["stop"], 100)
        self.assertEqual(info["step"], 5)
        self.assertIn("start", info["public_methods_and_attrs"])
        self.assertIn("stop", info["public_methods_and_attrs"])
        self.assertIn("step", info["public_methods_and_attrs"])
        self.assertIn("count", info["public_methods_and_attrs"])
        self.assertIn("index", info["public_methods_and_attrs"])
        self.assertTrue(info["is_range_iterator"])

    def test_document_python_version_evolution(self) -> None:
        """Verify version evolution notes map all major milestones from 2.7 to 3.13."""
        matrix = document_python_version_evolution()
        self.assertIn("Python 2.7", matrix)
        self.assertIn("Python 3.3-3.4", matrix)
        self.assertIn("Python 3.5-3.8", matrix)
        self.assertIn("Python 3.9-3.11", matrix)
        self.assertIn("Python 3.12-3.13", matrix)


if __name__ == "__main__":
    unittest.main()
