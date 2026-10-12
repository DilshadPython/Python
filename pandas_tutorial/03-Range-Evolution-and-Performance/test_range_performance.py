"""
Unit Test Suite for Pandas Range Evolution, Performance, and Introspection Module.

Tests date range sequence generation, category memory optimizations, speed benchmarks,
Python 3.3 to Python 3.13 evolution matrix, and reflection attributes.
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python search path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import pandas as pd

from date_range_vs_python_range import (
    generate_pandas_date_range,
    generate_pandas_range_index,
    generate_python_range,
)
from pandas_performance_and_evolution import (
    benchmark_pandas_vectorization,
    get_version_evolution_matrix,
    measure_category_memory_savings,
)
from reflection_and_introspection import (
    introspect_dataframe_attributes,
    introspect_series_attributes,
)


class TestPandasRangePerformanceAndEvolution(unittest.TestCase):
    """Test cases for date range vs range, category memory optimizations, and reflection."""

    def test_date_range_vs_python_range(self) -> None:
        """Verify date_range generation and RangeIndex."""
        py_r = generate_python_range(1, 10, 2)
        d_rng = generate_pandas_date_range("2026-01-01", periods=5, freq="D")
        r_idx = generate_pandas_range_index(0, 100, 5)

        self.assertEqual(list(py_r), [1, 3, 5, 7, 9])
        self.assertEqual(len(d_rng), 5)
        self.assertEqual(len(r_idx), 20)
        self.assertEqual(r_idx.step, 5)

    def test_category_memory_savings(self) -> None:
        """Verify memory reduction when casting to category dtype."""
        mem = measure_category_memory_savings(1_000)
        self.assertLess(mem["category_dtype_bytes"], mem["object_dtype_bytes"])
        self.assertGreater(mem["memory_savings_percent"], 0.0)

    def test_benchmark_vectorization(self) -> None:
        """Verify Pandas vectorization speedup benchmark."""
        bench = benchmark_pandas_vectorization(5_000)
        self.assertIn("pandas_vectorized_seconds", bench)
        self.assertGreater(bench["speedup_factor"], 0.0)

    def test_version_evolution_matrix(self) -> None:
        """Verify evolution matrix dictionary contains Python 3.3 to 3.13 keys."""
        evo = get_version_evolution_matrix()
        self.assertIn("Python 3.3", evo)
        self.assertIn("Python 3.5", evo)
        self.assertIn("Python 3.8", evo)
        self.assertIn("Python 3.11", evo)
        self.assertIn("Python 3.13", evo)

    def test_introspect_series(self) -> None:
        """Verify reflection output for pd.Series."""
        s = pd.Series(["A", "B", "A", "C"], name="TestCol")
        info = introspect_series_attributes(s)
        self.assertEqual(info["name"], "TestCol")
        self.assertEqual(info["nunique_count"], 3)
        self.assertEqual(info["value_counts"]["A"], 2)

    def test_introspect_dataframe(self) -> None:
        """Verify reflection output for pd.DataFrame."""
        df = pd.DataFrame({"X": [1, 2], "Y": [3, 4]})
        info = introspect_dataframe_attributes(df)
        self.assertEqual(info["shape"], (2, 2))
        self.assertEqual(info["transposed_shape"], (2, 2))


if __name__ == "__main__":
    unittest.main()
