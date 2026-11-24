"""
Unit Test Suite for Matplotlib Plotting and Graph Traversal Algorithms across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. Modular Matplotlib bar chart generation (`bar_chart_generator.py`).
2. Beginner level plot creation (`beginner_graph.py`).
3. Intermediate level horizontal plot styling (`intermediate_graph.py`).
4. Senior level Graph BFS/DFS traversal algorithms (`senior_graph.py`).
"""

import matplotlib
import sys
import tempfile
import unittest
from pathlib import Path

# Ensure headless Agg backend for non-interactive execution during unit tests
try:
    matplotlib.use("Agg")
except Exception:
    pass

# Support both package and local directory import paths
root = Path(__file__).parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from bar_chart_generator import render_bar_chart
from beginner_graph import generate_simple_bar_chart
from intermediate_graph import generate_horizontal_bar_chart
from senior_graph import Graph, render_graph_algorithm_comparison


class TestGraphAlgorithms(unittest.TestCase):
    """Test suite verifying graph plotting and traversal algorithms."""

    def test_render_bar_chart(self) -> None:
        """Verify modular render_bar_chart figure creation and file saving."""
        categories = ["A", "B", "C"]
        values = [10, 20, 30]

        with tempfile.TemporaryDirectory() as temp_dir:
            out_file = str(Path(temp_dir) / "chart.png")
            fig = render_bar_chart(categories, values, output_filename=out_file)
            self.assertIsNotNone(fig)
            self.assertTrue(Path(out_file).exists())

    def test_beginner_graph(self) -> None:
        """Verify beginner generate_simple_bar_chart figure creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            out_file = str(Path(temp_dir) / "beginner.png")
            generate_simple_bar_chart(["X", "Y"], [5, 15], output_filename=out_file)
            self.assertTrue(Path(out_file).exists())

    def test_intermediate_graph(self) -> None:
        """Verify intermediate generate_horizontal_bar_chart figure creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            out_file = str(Path(temp_dir) / "intermediate.png")
            generate_horizontal_bar_chart(["Tech1", "Tech2"], [40, 80], output_filename=out_file)
            self.assertTrue(Path(out_file).exists())

    def test_senior_graph_algorithms(self) -> None:
        """Verify senior Graph BFS and DFS traversal algorithms."""
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")

        bfs_order = g.breadth_first_search("A")
        self.assertEqual(bfs_order, ["A", "B", "C", "D"])

        dfs_order = g.depth_first_search("A")
        self.assertEqual(dfs_order[0], "A")
        self.assertEqual(len(dfs_order), 4)

        with tempfile.TemporaryDirectory() as temp_dir:
            out_file = str(Path(temp_dir) / "senior.png")
            render_graph_algorithm_comparison(bfs_order, dfs_order, output_filename=out_file)
            self.assertTrue(Path(out_file).exists())


if __name__ == "__main__":
    unittest.main()
