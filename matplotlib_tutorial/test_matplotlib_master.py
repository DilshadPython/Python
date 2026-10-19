"""
Master Test Suite Runner for Matplotlib Core Tutorial.
Verifies thread-safe headless ('Agg') rendering, base64 chart data generation,
multi-axis dashboards, 3D surface visualizations, and memory leak prevention.
"""

from pathlib import Path
import sys
import unittest

# Ensure current directory is on python path for local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from matplotlib_basics import (
    generate_line_and_sine_plot,
    generate_bar_and_performance_plot,
    generate_multiaxis_dashboard,
    generate_3d_surface_plot,
    generate_status_observability_dashboard,
    render_preset,
)


class TestMatplotlibTutorial(unittest.TestCase):
    """Unit test suite verifying headless Matplotlib base64 image generation."""

    def test_line_and_sine_plot(self):
        res = generate_line_and_sine_plot()
        self.assertEqual(res["plot_type"], "line_signal")
        self.assertGreater(len(res["image_base64"]), 1000)
        self.assertGreater(res["data_points"], 100)

    def test_bar_and_performance_plot(self):
        res = generate_bar_and_performance_plot()
        self.assertEqual(res["plot_type"], "bar_benchmark")
        self.assertEqual(len(res["frameworks"]), 4)
        self.assertGreater(res["speedup_vs_pure_python"], 10.0)
        self.assertGreater(len(res["image_base64"]), 1000)

    def test_multiaxis_dashboard(self):
        res = generate_multiaxis_dashboard()
        self.assertEqual(res["plot_type"], "multiaxis_dashboard")
        self.assertEqual(res["panels_count"], 4)
        self.assertGreater(len(res["image_base64"]), 1000)

    def test_3d_surface_plot(self):
        res = generate_3d_surface_plot()
        self.assertEqual(res["plot_type"], "3d_surface")
        self.assertIn("optimal_point", res)
        self.assertGreater(len(res["image_base64"]), 5000)

    def test_status_observability_dashboard(self):
        res = generate_status_observability_dashboard()
        self.assertEqual(res["plot_type"], "status_observability_dashboard")
        self.assertEqual(res["services_monitored"], 4)
        self.assertGreater(res["pipeline_total_ms"], 0)
        self.assertGreater(len(res["image_base64"]), 5000)

    def test_render_preset_dispatch(self):
        p1 = render_preset(1)
        self.assertEqual(p1["plot_type"], "line_signal")
        self.assertIn("duration_ms", p1)

        p2 = render_preset(2)
        self.assertEqual(p2["plot_type"], "bar_benchmark")

        p3 = render_preset(3)
        self.assertEqual(p3["plot_type"], "multiaxis_dashboard")

        p4 = render_preset(4)
        self.assertEqual(p4["plot_type"], "3d_surface")


if __name__ == "__main__":
    unittest.main()
