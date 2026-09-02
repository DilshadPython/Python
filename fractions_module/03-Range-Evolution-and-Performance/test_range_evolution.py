"""
Unit test suite for Step 3: Range Evolution, Memory Benchmark, & Reflection.
"""
# "import unittest" loads unit testing framework.
import unittest
# "from fractions import Fraction" imports rational fraction class.
from fractions import Fraction

# "from fraction_range_evolution import ..." imports range evolution helpers.
from fraction_range_evolution import (
    generate_fractional_range,
    compare_range_and_fraction_memory_efficiency,
    inspect_range_attributes_and_methods,
    document_python_version_evolution,
)


class TestFractionRangeEvolution(unittest.TestCase):
    """
    Test suite verifying fractional range generation, memory efficiency, range introspection, and version matrix.
    """

    def test_generate_fractional_range_positive_step(self) -> None:
        """Verify fractional range generation with positive step."""
        f_range = generate_fractional_range(Fraction(0, 1), Fraction(1, 1), Fraction(1, 4))
        expected = [Fraction(0, 1), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
        self.assertEqual(f_range, expected)

    def test_generate_fractional_range_negative_step(self) -> None:
        """Verify fractional range generation with negative step."""
        f_range = generate_fractional_range(Fraction(1, 1), Fraction(0, 1), Fraction(-1, 4))
        expected = [Fraction(1, 1), Fraction(3, 4), Fraction(1, 2), Fraction(1, 4)]
        self.assertEqual(f_range, expected)

    def test_compare_range_and_fraction_memory_efficiency(self) -> None:
        """Verify O(1) RAM footprint for range objects relative to list."""
        mem_info = compare_range_and_fraction_memory_efficiency(500)
        self.assertTrue(mem_info["is_range_constant_memory"])
        self.assertLess(mem_info["range_bytes"], mem_info["fraction_list_bytes"])

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
        self.assertTrue(info["containment_check_50"])

    def test_document_python_version_evolution(self) -> None:
        """Verify version evolution notes map all major milestones from 2.7 to 3.13."""
        matrix = document_python_version_evolution()
        self.assertIn("Python 2.7", matrix)
        self.assertIn("Python 3.0-3.4", matrix)
        self.assertIn("Python 3.5-3.8", matrix)
        self.assertIn("Python 3.9-3.11", matrix)
        self.assertIn("Python 3.12-3.13", matrix)


if __name__ == "__main__":
    unittest.main()
