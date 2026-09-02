"""
Unit Test Suite for Range Evolution, Performance, and Introspection Module.

Tests range vs arange behaviors, memory footprint measurements, benchmark functionality,
and reflection matrices (dir(range) and dir(np.ndarray)).
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python search path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import numpy as np

from arange_vs_range import (
    demonstrate_floating_and_negative_steps,
    generate_numpy_arange,
    generate_python_range,
)
from range_performance_and_evolution import (
    benchmark_iteration_performance,
    get_version_evolution_matrix,
    measure_memory_footprint,
)
from reflection_and_introspection import (
    introspect_ndarray_attributes,
    introspect_range_attributes,
)


class TestRangePerformanceAndEvolution(unittest.TestCase):
    """Test cases for range vs arange, performance metrics, and reflection."""

    def test_range_vs_arange_generation(self) -> None:
        """Verify Python range vs NumPy arange generation."""
        py_r = generate_python_range(1, 10, 2)
        np_r = generate_numpy_arange(1, 10, 2)

        self.assertEqual(list(py_r), [1, 3, 5, 7, 9])
        self.assertEqual(list(np_r), [1, 3, 5, 7, 9])

    def test_floating_and_negative_steps(self) -> None:
        """Verify float steps and negative steps in np.arange."""
        flt_arr, neg_arr = demonstrate_floating_and_negative_steps()
        self.assertTrue(np.allclose(flt_arr, [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]))
        self.assertEqual(neg_arr[0], 101)
        self.assertEqual(neg_arr[1], 96)

    def test_measure_memory_footprint(self) -> None:
        """Verify memory measurement functions."""
        stats = measure_memory_footprint(10_000)
        self.assertIn("range_object_bytes", stats)
        self.assertIn("numpy_array_bytes", stats)
        # O(1) range memory footprint should be substantially smaller than O(N) array buffer
        self.assertLess(stats["range_object_bytes"], stats["numpy_array_bytes"])

    def test_benchmark_performance(self) -> None:
        """Verify performance benchmark execution."""
        perf = benchmark_iteration_performance(10_000)
        self.assertIn("python_range_sum_seconds", perf)
        self.assertIn("numpy_array_sum_seconds", perf)
        self.assertGreater(perf["speedup_factor"], 0.0)

    def test_version_evolution_matrix(self) -> None:
        """Verify Python 3.3 to Python 3.13 evolution matrix dictionary keys."""
        evo = get_version_evolution_matrix()
        self.assertIn("Python 3.3", evo)
        self.assertIn("Python 3.5", evo)
        self.assertIn("Python 3.8", evo)
        self.assertIn("Python 3.11", evo)
        self.assertIn("Python 3.13", evo)

    def test_introspect_range_attributes(self) -> None:
        """Verify reflection output for dir(range)."""
        info = introspect_range_attributes()
        self.assertEqual(info["start"], 10)
        self.assertEqual(info["stop"], 100)
        self.assertEqual(info["step"], 5)
        self.assertIn("count", info["public_attributes"])
        self.assertIn("index", info["public_attributes"])

    def test_introspect_ndarray_attributes(self) -> None:
        """Verify reflection and statistics for dir(np.ndarray)."""
        mat = np.array([[10, 20], [30, 40]])
        info = introspect_ndarray_attributes(mat)
        self.assertEqual(info["sum"], 100.0)
        self.assertEqual(info["mean"], 25.0)
        self.assertEqual(info["max"], 40.0)
        self.assertEqual(info["min"], 10.0)
        self.assertEqual(info["argmax"], 3)
        self.assertEqual(info["argmin"], 0)
        self.assertEqual(info["flattened_list"], [10, 20, 30, 40])


if __name__ == "__main__":
    unittest.main()
