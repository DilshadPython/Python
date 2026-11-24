"""
Unit Test Suite for Calculation Range Performance, Introspection, and Version Evolution.

Tests range schedule generation, O(1) memory efficiency, dir(range) reflection matrix,
and version evolution mapping.
"""

import unittest

from range_calculator_performance import (
    compare_range_vs_list_memory,
    generate_schedule_month_range,
    get_calculation_version_evolution_matrix,
    inspect_range_attributes,
)


class TestRangeCalculatorEvolution(unittest.TestCase):
    """Test cases for range schedule generation, memory benchmarks, and reflection matrix."""

    def test_generate_schedule_month_range(self) -> None:
        """Verify schedule month range sequence generation (1..N)."""
        months = generate_schedule_month_range(total_months=12)
        self.assertEqual(months.start, 1)
        self.assertEqual(months.stop, 13)
        self.assertEqual(months.step, 1)
        self.assertEqual(list(months), list(range(1, 13)))

    def test_dir_range_reflection_matrix(self) -> None:
        """Verify dir(range) reflection matrix contains expected methods."""
        r_obj = range(1, 24, 1)
        info = inspect_range_attributes(r_obj)

        self.assertEqual(info["start"], 1)
        self.assertEqual(info["stop"], 24)
        self.assertEqual(info["step"], 1)
        self.assertTrue(info["has_count"])
        self.assertTrue(info["has_index"])
        self.assertIn("start", info["public_members"])
        self.assertIn("stop", info["public_members"])
        self.assertIn("step", info["public_members"])
        self.assertIn("count", info["public_members"])
        self.assertIn("index", info["public_members"])

    def test_memory_efficiency_comparison(self) -> None:
        """Verify range memory footprint O(1) is significantly smaller than list O(N)."""
        r_bytes, l_bytes = compare_range_vs_list_memory(50_000)
        self.assertLess(r_bytes, 100)  # ~48 bytes for range sequence
        self.assertGreater(l_bytes, 8000)  # > 8KB for list

    def test_version_evolution_matrix_keys(self) -> None:
        """Verify version evolution matrix contains key Python release notes."""
        matrix = get_calculation_version_evolution_matrix()
        self.assertIn("Python 2.7 (Numeric Legacy)", matrix)
        self.assertIn("Python 3.0-3.3", matrix)
        self.assertIn("Python 3.5", matrix)
        self.assertIn("Python 3.8", matrix)
        self.assertIn("Python 3.11", matrix)
        self.assertIn("Python 3.13", matrix)


if __name__ == "__main__":
    unittest.main()
