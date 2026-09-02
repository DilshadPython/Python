"""
Unit Test Suite for Range Evolution, Performance, and Reflection Module.

Tests local vs global execution benchmarks, Python 3.3 to 3.13 evolution matrix,
module attribute reflection, and dir(range) introspection.
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python search path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from execution_performance_and_evolution import (
    benchmark_local_vs_global_execution,
    get_version_evolution_matrix,
)
from range_iteration_and_entry_points import process_range_in_local_scope
from reflection_and_introspection import (
    introspect_module_attributes,
    introspect_range_attributes,
)


class TestNameMainRangePerformanceAndEvolution(unittest.TestCase):
    """Test cases for range iteration, local scope benchmarks, and reflection."""

    def test_process_range_in_local_scope(self) -> None:
        """Verify range processing math inside function scope."""
        total = process_range_in_local_scope(100)
        self.assertEqual(total, sum(range(100)))

    def test_benchmark_local_vs_global_execution(self) -> None:
        """Verify performance benchmark dictionary."""
        bench = benchmark_local_vs_global_execution(1_000)
        self.assertIn("local_scope_seconds", bench)
        self.assertIn("global_scope_seconds", bench)
        self.assertGreaterEqual(bench["local_speedup_factor"], 0.0)

    def test_version_evolution_matrix(self) -> None:
        """Verify evolution matrix dictionary contains Python 3.3 to 3.13 keys."""
        evo = get_version_evolution_matrix()
        self.assertIn("Python 3.3", evo)
        self.assertIn("Python 3.5", evo)
        self.assertIn("Python 3.8", evo)
        self.assertIn("Python 3.11", evo)
        self.assertIn("Python 3.13", evo)

    def test_introspect_module_attributes(self) -> None:
        """Verify module introspection via dir()."""
        info = introspect_module_attributes()
        self.assertGreater(info["attribute_count"], 0)

    def test_introspect_range_attributes(self) -> None:
        """Verify range introspection dir(range)."""
        info = introspect_range_attributes()
        self.assertEqual(info["start"], 10)
        self.assertEqual(info["stop"], 100)
        self.assertEqual(info["step"], 5)
        self.assertIn("count", info["public_attribute_list"])
        self.assertIn("index", info["public_attribute_list"])


if __name__ == "__main__":
    unittest.main()
