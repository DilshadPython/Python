"""
Unit Test Suite for Range Evolution, Introspection, and Performance Benchmarks.

Tests CLI range construction, O(1) memory efficiency, dir(range) reflection matrix,
and version evolution records.
"""

# Standard library test framework imports
import unittest
from typing import List

# Import target functions from range_argparse module
from range_argparse import (
    build_range_from_cli,
    compare_range_vs_list_memory,
    get_version_evolution_matrix,
    inspect_range_attributes,
)


class TestRangeEvolution(unittest.TestCase):
    """Test cases for range CLI parser, memory benchmarks, and reflection matrix."""

    def test_build_range_from_cli_valid(self) -> None:
        """Verify range object creation from valid CLI argument inputs."""
        args_input: List[str] = ["--start", "5", "--stop", "50", "--step", "5"]
        r_obj, meta = build_range_from_cli(args_input)

        self.assertEqual(r_obj.start, 5)
        self.assertEqual(r_obj.stop, 50)
        self.assertEqual(r_obj.step, 5)
        self.assertEqual(len(r_obj), 9)
        self.assertEqual(meta["start"], 5)
        self.assertEqual(meta["stop"], 50)
        self.assertEqual(meta["step"], 5)
        self.assertIn("count", meta["public_members"])
        self.assertIn("index", meta["public_members"])

    def test_zero_step_raises_value_error(self) -> None:
        """Verify step value of zero raises ValueError."""
        args_input: List[str] = ["--stop", "10", "--step", "0"]
        with self.assertRaises(ValueError):
            build_range_from_cli(args_input)

    def test_dir_range_reflection_matrix(self) -> None:
        """Verify dir(range) introspection matrix contains expected attributes and methods."""
        r_obj = range(0, 100, 2)
        info = inspect_range_attributes(r_obj)

        self.assertEqual(info["start"], 0)
        self.assertEqual(info["stop"], 100)
        self.assertEqual(info["step"], 2)
        self.assertTrue(info["count_methods"])
        self.assertTrue(info["index_methods"])
        self.assertIn("start", info["public_members"])
        self.assertIn("stop", info["public_members"])
        self.assertIn("step", info["public_members"])
        self.assertIn("count", info["public_members"])
        self.assertIn("index", info["public_members"])

    def test_memory_efficiency_comparison(self) -> None:
        """Verify range O(1) memory footprint is significantly smaller than list O(N)."""
        r_bytes, l_bytes = compare_range_vs_list_memory(50_000)
        self.assertLess(r_bytes, 100)  # ~48 bytes for range object
        self.assertGreater(l_bytes, 100_000)  # > 400KB for 50k integer list

    def test_version_evolution_matrix_keys(self) -> None:
        """Verify version evolution matrix contains all key Python milestones."""
        matrix = get_version_evolution_matrix()
        self.assertIn("Python 2.7", matrix)
        self.assertIn("Python 3.0-3.2", matrix)
        self.assertIn("Python 3.7", matrix)
        self.assertIn("Python 3.9", matrix)
        self.assertIn("Python 3.10", matrix)
        self.assertIn("Python 3.11", matrix)
        self.assertIn("Python 3.13", matrix)


if __name__ == "__main__":
    unittest.main()
