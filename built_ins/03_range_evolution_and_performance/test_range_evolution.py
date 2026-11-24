"""
Unit Test Suite for Built-in Range Performance, Introspection, and Version Evolution.

Tests range sequence generation, O(1) memory efficiency, dir(range) reflection matrix,
and version evolution mapping.
"""

import unittest

from range_builtin_performance import (
    compare_range_vs_list_memory,
    generate_builtin_step_sequence,
    get_builtin_version_evolution_matrix,
    inspect_range_attributes,
)


class TestRangeBuiltinEvolution(unittest.TestCase):
    """Test cases for range sequence generation, memory benchmarks, and reflection matrix."""

    def test_generate_builtin_step_sequence(self) -> None:
        """Verify built-in step sequence generation."""
        seq = generate_builtin_step_sequence(0, 100, 25)
        self.assertEqual(seq.start, 0)
        self.assertEqual(seq.stop, 100)
        self.assertEqual(seq.step, 25)
        self.assertEqual(list(seq), [0, 25, 50, 75])

    def test_dir_range_reflection_matrix(self) -> None:
        """Verify dir(range) reflection matrix contains expected methods."""
        r_obj = range(0, 50, 5)
        info = inspect_range_attributes(r_obj)

        self.assertEqual(info["start"], 0)
        self.assertEqual(info["stop"], 50)
        self.assertEqual(info["step"], 5)
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
        matrix = get_builtin_version_evolution_matrix()
        self.assertIn("Python 2.7 (Built-in Legacy)", matrix)
        self.assertIn("Python 3.0-3.3", matrix)
        self.assertIn("Python 3.8", matrix)
        self.assertIn("Python 3.10", matrix)
        self.assertIn("Python 3.11", matrix)
        self.assertIn("Python 3.13", matrix)


if __name__ == "__main__":
    unittest.main()
