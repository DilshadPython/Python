"""
Senior Level Graph Algorithms & Visualizations Module (`senior_graph.py`).

This module provides graph algorithm structures designed for senior software engineers
(Adjacency List `Graph` class, Breadth-First Search BFS, Depth-First Search DFS, multi-subplot Matplotlib figures).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from collections import deque`: Double-ended queue for O(1) BFS traversal operations.
# - `import matplotlib`: Core Matplotlib plotting framework.
# - `import matplotlib.pyplot as plt`: Subplot visualization interface.
# - `import sys`: System execution status utilities.
# - `from typing import Dict, List, Set`: PEP 484 type hint generics.
# =========================================================================
from collections import deque
import matplotlib
import sys
from typing import Dict, List, Set

# Ensure headless Agg backend for non-interactive execution
try:
    matplotlib.use("Agg")
except Exception:
    pass

import matplotlib.pyplot as plt


class Graph:
    """Adjacency List Graph Data Structure supporting directed and undirected edges."""

    def __init__(self) -> None:
        """Initialize empty graph adjacency list mapping."""
        self.adj_list: Dict[str, List[str]] = {}

    def add_edge(self, source: str, destination: str, bidirectional: bool = True) -> None:
        """Add edge between source and destination nodes.

        Args:
            source (str): Source node identifier.
            destination (str): Destination node identifier.
            bidirectional (bool): Whether edge is undirected (both directions).
        """
        self.adj_list.setdefault(source, []).append(destination)
        if bidirectional:
            self.adj_list.setdefault(destination, []).append(source)
        else:
            self.adj_list.setdefault(destination, [])

    def breadth_first_search(self, start_node: str) -> List[str]:
        """Perform Breadth-First Search (BFS) graph traversal starting at start_node.

        Args:
            start_node (str): Starting node identifier.

        Returns:
            List[str]: Order of nodes visited during BFS traversal.
        """
        if start_node not in self.adj_list:
            return []

        visited: Set[str] = {start_node}
        queue: deque[str] = deque([start_node])
        traversal_order: List[str] = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def depth_first_search(self, start_node: str) -> List[str]:
        """Perform Depth-First Search (DFS) graph traversal starting at start_node.

        Args:
            start_node (str): Starting node identifier.

        Returns:
            List[str]: Order of nodes visited during DFS traversal.
        """
        if start_node not in self.adj_list:
            return []

        visited: Set[str] = set()
        traversal_order: List[str] = []

        def _dfs(current: str) -> None:
            visited.add(current)
            traversal_order.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start_node)
        return traversal_order


def render_graph_algorithm_comparison(
    bfs_order: List[str],
    dfs_order: List[str],
    output_filename: str = "senior_graph_algorithm_comparison.png",
) -> None:
    """Render multi-panel Matplotlib subplot comparing BFS and DFS traversal step orders.

    Args:
        bfs_order (List[str]): List of nodes visited during BFS.
        dfs_order (List[str]): List of nodes visited during DFS.
        output_filename (str): Image output path.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    steps = list(range(1, len(bfs_order) + 1))

    ax1.bar(bfs_order, steps, color="#4CAF50")
    ax1.set_title("Breadth-First Search (BFS) Traversal Order", fontsize=12)
    ax1.set_ylabel("Step Order Sequence")

    ax2.bar(dfs_order, steps, color="#FF9800")
    ax2.set_title("Depth-First Search (DFS) Traversal Order", fontsize=12)
    ax2.set_ylabel("Step Order Sequence")

    plt.tight_layout()
    fig.savefig(output_filename, dpi=200)
    plt.close(fig)

    print(f"Senior graph traversal plot saved to '{output_filename}'")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior graph algorithms demonstration."""
    print("=== Senior Level Graph Algorithms & Multi-Panel Visualization ===")

    g = Graph()
    g.add_edge("Python", "Django")
    g.add_edge("Python", "Flask")
    g.add_edge("Django", "PostgreSQL")
    g.add_edge("Flask", "SQLAlchemy")
    g.add_edge("Data Science", "Python")

    bfs_res = g.breadth_first_search("Data Science")
    dfs_res = g.depth_first_search("Data Science")

    print(f"BFS Traversal Order: {bfs_res}")
    print(f"DFS Traversal Order: {dfs_res}")

    render_graph_algorithm_comparison(bfs_res, dfs_res)
    return 0


if __name__ == "__main__":
    sys.exit(main())
