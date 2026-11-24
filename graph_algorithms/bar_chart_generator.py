"""
Bar Chart Generator Module (`bar_chart_generator.py`).

This module provides reusable helper functions for rendering, customizing, and saving
bar charts using `matplotlib.pyplot`.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import matplotlib`: Core Matplotlib plotting framework.
# - `import matplotlib.pyplot as plt`: State-based interface for plot visualization.
# - `import sys`: System utilities for execution status.
# - `from typing import Any, List, Optional, Union`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Any, List, Optional, Union
from unittest.mock import MagicMock

try:
    import matplotlib

    matplotlib.use("Agg")  # Set non-interactive Agg backend for headless systems
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib = MagicMock()  # type: ignore
    plt = MagicMock()  # type: ignore


def render_bar_chart(
    categories: List[str],
    values: List[Union[int, float]],
    title: str = "Book Library",
    xlabel: str = "Books",
    ylabel: str = "Status",
    color: str = "green",
    output_filename: Optional[str] = None,
    show_plot: bool = False,
) -> Any:
    """Render a Matplotlib vertical bar chart with titles and labels.

    Args:
        categories (List[str]): List of category or book names.
        values (List[Union[int, float]]): Data values corresponding to each category.
        title (str): Plot title string. Defaults to "Book Library".
        xlabel (str): X-axis label string. Defaults to "Books".
        ylabel (str): Y-axis label string. Defaults to "Status".
        color (str): Bar color hex or name string. Defaults to "green".
        output_filename (Optional[str]): File path to save plot image (e.g. "chart.png").
        show_plot (bool): Whether to trigger interactive plt.show() popup window.

    Returns:
        Any: Matplotlib Figure instance or mock handle.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(categories, values, color=color)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)

    plt.tight_layout()

    if output_filename:
        fig.savefig(output_filename, dpi=300)
        print(f"Saved bar chart plot to '{output_filename}'")

    if show_plot:
        plt.show()

    return fig


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for bar chart generator demonstration."""
    print("=== Matplotlib Bar Chart Generator Demonstration ===")

    books = ["Data Science", "Biology", "Chemistry", "Python Tutorials", "Django Projects"]
    read_counts = [12, 45, 73, 23, 42]

    render_bar_chart(
        categories=books,
        values=read_counts,
        title="Book Library Read Status",
        output_filename="book_library_chart.png",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
