"""
Unit Test Suite for Range API Pagination, Introspection, and Performance Benchmarks.

Tests range pagination sequence generation, O(1) memory efficiency, dir(range) reflection matrix,
and version evolution mapping.
"""

import unittest
from typing import List

from range_api_pagination import (
    compare_range_vs_list_memory,
    generate_pagination_offsets,
    get_version_evolution_matrix,
    inspect_range_attributes,
    simulate_paginated_api_fetch,
)


class TestRangeApiEvolution(unittest.TestCase):
    """Test cases for range API pagination, memory benchmarks, and reflection matrix."""

    def test_generate_pagination_offsets(self) -> None:
        """Verify range pagination sequence generation."""
        offsets = generate_pagination_offsets(total_records=100, page_size=25)
        self.assertEqual(offsets.start, 0)
        self.assertEqual(offsets.stop, 100)
        self.assertEqual(offsets.step, 25)
        self.assertEqual(list(offsets), [0, 25, 50, 75])

    def test_simulate_paginated_api_fetch(self) -> None:
        """Verify generator simulation of paginated API requests."""
        pages = list(simulate_paginated_api_fetch(total_items=70, page_size=25))
        self.assertEqual(len(pages), 3)
        self.assertEqual(pages[0], {"page": 1, "offset": 0, "limit": 25, "items_retrieved": 25})
        self.assertEqual(pages[1], {"page": 2, "offset": 25, "limit": 25, "items_retrieved": 25})
        self.assertEqual(pages[2], {"page": 3, "offset": 50, "limit": 25, "items_retrieved": 20})

    def test_dir_range_reflection_matrix(self) -> None:
        """Verify dir(range) reflection matrix contains expected methods."""
        r_obj = range(0, 100, 10)
        info = inspect_range_attributes(r_obj)

        self.assertEqual(info["start"], 0)
        self.assertEqual(info["stop"], 100)
        self.assertEqual(info["step"], 10)
        self.assertTrue(info["has_count"])
        self.assertTrue(info["has_index"])
        self.assertIn("start", info["public_members"])
        self.assertIn("stop", info["public_members"])
        self.assertIn("step", info["public_members"])
        self.assertIn("count", info["public_members"])
        self.assertIn("index", info["public_members"])

    def test_memory_efficiency_comparison(self) -> None:
        """Verify range memory footprint O(1) is significantly smaller than list O(N)."""
        r_bytes, l_bytes = compare_range_vs_list_memory(20_000)
        self.assertLess(r_bytes, 100)  # ~48 bytes for range sequence
        self.assertGreater(l_bytes, 50_000)  # > 100KB for list

    def test_version_evolution_matrix_keys(self) -> None:
        """Verify version evolution matrix contains key Python release notes."""
        matrix = get_version_evolution_matrix()
        self.assertIn("Python 2.7", matrix)
        self.assertIn("Python 3.0-3.3", matrix)
        self.assertIn("Python 3.5", matrix)
        self.assertIn("Python 3.7", matrix)
        self.assertIn("Python 3.11", matrix)
        self.assertIn("Python 3.13", matrix)


if __name__ == "__main__":
    unittest.main()
