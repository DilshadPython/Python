"""
Unit Test Suite for Range Conda Performance, Introspection, and Version Evolution.

Tests range pagination sequence generation, O(1) memory efficiency, dir(range) reflection matrix,
and version evolution mapping.
"""

import unittest

from range_conda_performance import (
    compare_range_vs_list_memory,
    generate_package_pagination_offsets,
    get_version_evolution_matrix,
    inspect_range_attributes,
    simulate_conda_package_batch_fetch,
)


class TestRangeCondaEvolution(unittest.TestCase):
    """Test cases for range package pagination, memory benchmarks, and reflection matrix."""

    def test_generate_package_pagination_offsets(self) -> None:
        """Verify range package offset sequence generation."""
        offsets = generate_package_pagination_offsets(total_packages=200, batch_size=50)
        self.assertEqual(offsets.start, 0)
        self.assertEqual(offsets.stop, 200)
        self.assertEqual(offsets.step, 50)
        self.assertEqual(list(offsets), [0, 50, 100, 150])

    def test_simulate_conda_package_batch_fetch(self) -> None:
        """Verify generator simulation of paginated Conda package batches."""
        batches = list(simulate_conda_package_batch_fetch(total_packages=120, batch_size=50))
        self.assertEqual(len(batches), 3)
        self.assertEqual(batches[0], {"batch": 1, "start_offset": 0, "end_offset": 50, "batch_count": 50})
        self.assertEqual(batches[1], {"batch": 2, "start_offset": 50, "end_offset": 100, "batch_count": 50})
        self.assertEqual(batches[2], {"batch": 3, "start_offset": 100, "end_offset": 120, "batch_count": 20})

    def test_dir_range_reflection_matrix(self) -> None:
        """Verify dir(range) reflection matrix contains expected methods."""
        r_obj = range(0, 500, 50)
        info = inspect_range_attributes(r_obj)

        self.assertEqual(info["start"], 0)
        self.assertEqual(info["stop"], 500)
        self.assertEqual(info["step"], 50)
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
        matrix = get_version_evolution_matrix()
        self.assertIn("Python 2.7 (env27)", matrix)
        self.assertIn("Python 3.0-3.3", matrix)
        self.assertIn("Python 3.10 (env310)", matrix)
        self.assertIn("Python 3.11", matrix)
        self.assertIn("Python 3.13", matrix)


if __name__ == "__main__":
    unittest.main()
