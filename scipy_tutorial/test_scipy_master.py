"""
Master Test Suite Runner for SciPy Core Tutorial.
Verifies fundamental constants, sparse matrix representation, non-linear curve fitting,
numerical quadrature, ODE solvers, signal processing, and inferential statistics.
"""

from pathlib import Path
import sys
import unittest

# Ensure current directory is on python path for local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from scipy_basics import (
    demonstrate_01_constants_and_sparse,
    demonstrate_02_optimization_and_fitting,
    demonstrate_02_integration_and_ode,
    demonstrate_03_signal_and_stats,
    run_all_scipy_demos,
)


class TestSciPyTutorial(unittest.TestCase):
    """Unit test suite verifying the SciPy scientific computing tutorial module."""

    def test_constants_and_sparse(self):
        res = demonstrate_01_constants_and_sparse()
        self.assertAlmostEqual(res["speed_of_light_m_s"], 299792458.0, places=1)
        self.assertAlmostEqual(res["gravity_m_s2"], 9.80665, places=3)
        self.assertEqual(res["sparse_non_zeros"], 3)
        self.assertGreater(res["memory_saving_ratio"], 10.0)

    def test_optimization_and_fitting(self):
        res = demonstrate_02_optimization_and_fitting()
        self.assertAlmostEqual(res["minimized_x"], 3.0, places=2)
        self.assertAlmostEqual(res["minimum_value"], 4.0, places=2)
        self.assertTrue(res["root_converged"])
        self.assertAlmostEqual(res["root_x"], 2.0946, places=2)

    def test_integration_and_ode(self):
        res = demonstrate_02_integration_and_ode()
        self.assertAlmostEqual(res["definite_integral_sin_0_pi"], 2.0, places=4)
        self.assertEqual(len(res["ode_time_steps"]), 6)
        self.assertLess(res["ode_final_value"], 100.0)

    def test_signal_and_stats(self):
        res = demonstrate_03_signal_and_stats()
        self.assertLess(res["noise_variance_after"], res["noise_variance_before"])
        self.assertEqual(res["dominant_frequency_hz"], 5.0)
        self.assertTrue(res["is_statistically_significant"])

    def test_run_all_scipy_demos(self):
        agg = run_all_scipy_demos()
        self.assertEqual(agg["status"], "success")
        self.assertIn("scipy_version", agg)
        self.assertGreater(agg["duration_ms"], 0.0)


if __name__ == "__main__":
    unittest.main()
