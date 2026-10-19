"""
Master Test Suite for Scientific Python & PyData Stack Hub.
Executes comprehensive regression and functional tests across all four core pillars:
- NumPy (Vectorization & Contiguous Memory)
- Pandas (Tabular Analytics & GroupBy)
- SciPy (Numerical Algorithms & Physical Constants)
- Matplotlib (Headless Image Generation & Observability Dashboards)
"""

from pathlib import Path
import sys
import unittest

# Ensure current directory is on python path for local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from numpy_basics import (
    demonstrate_01_fundamentals_creation,
    demonstrate_02_advanced_math_and_ufuncs,
    demonstrate_03_range_performance_and_evolution,
)
from pandas_basics import (
    create_series_from_list,
    create_sample_dataframe,
    calculate_group_aggregations,
)
from scipy_basics import (
    demonstrate_01_constants_and_sparse,
    demonstrate_02_optimization_and_fitting,
    demonstrate_03_signal_and_stats,
    run_all_scipy_demos,
)
from matplotlib_basics import (
    generate_line_and_sine_plot,
    generate_bar_and_performance_plot,
    generate_multiaxis_dashboard,
)


class TestScientificPyDataStack(unittest.TestCase):
    """Integrated tests across the full PyData Big Four curriculum."""

    def test_numpy_operations(self):
        f = demonstrate_01_fundamentals_creation()
        self.assertIn("1d_array", f)
        m = demonstrate_02_advanced_math_and_ufuncs()
        self.assertIn("sqrt_vals", m)
        self.assertTrue(m["matrices_equal"])
        r = demonstrate_03_range_performance_and_evolution()
        self.assertGreater(r["speedup_factor"], 1.0)

    def test_pandas_operations(self):
        s = create_series_from_list()
        self.assertEqual(len(s), 5)
        df = create_sample_dataframe()
        self.assertEqual(len(df), 5)
        agg = calculate_group_aggregations(df, group_col="Department", target_col="Salary")
        self.assertGreater(len(agg), 0)

    def test_scipy_operations(self):
        sparse_res = demonstrate_01_constants_and_sparse()
        self.assertEqual(sparse_res["sparse_non_zeros"], 3)
        opt_res = demonstrate_02_optimization_and_fitting()
        self.assertTrue(opt_res["root_converged"])
        all_res = run_all_scipy_demos()
        self.assertEqual(all_res["status"], "success")

    def test_matplotlib_operations(self):
        p1 = generate_line_and_sine_plot()
        self.assertEqual(p1["plot_type"], "line_signal")
        self.assertGreater(len(p1["image_base64"]), 1000)
        p2 = generate_bar_and_performance_plot()
        self.assertEqual(p2["plot_type"], "bar_benchmark")
        p3 = generate_multiaxis_dashboard()
        self.assertEqual(p3["panels_count"], 4)


if __name__ == "__main__":
    unittest.main()
