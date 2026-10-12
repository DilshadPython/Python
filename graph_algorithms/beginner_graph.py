"""
Beginner Level Bar Plot Demonstration Module (`beginner_graph.py`).

This module provides clear, well-commented examples of basic `matplotlib.pyplot` bar chart
generation designed for beginner developers (`plt.bar`, `plt.title`, `plt.xlabel`, `plt.ylabel`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import matplotlib`: Core Matplotlib plotting library.
# - `import matplotlib.pyplot as plt`: State-based plotting interface.
# - `import sys`: System utilities for CLI execution exit status.
# =========================================================================
import matplotlib
import sys

# Ensure headless Agg backend for non-interactive execution
try:
    matplotlib.use("Agg")
except Exception:
    pass

import matplotlib.pyplot as plt


def generate_simple_bar_chart(
    categories: list[str],
    counts: list[int],
    output_filename: str = "beginner_bar_chart.png",
) -> None:
    """Generate and save a simple vertical bar chart.

    Args:
        categories (list[str]): List of category label strings.
        counts (list[int]): Numerical value counts corresponding to categories.
        output_filename (str): Target PNG image output path.
    """
    # 1. Create a bar chart with green bars
    plt.bar(categories, counts, color="green")

    # 2. Add chart metadata titles and labels
    plt.title("Book Library", fontsize=14)
    plt.xlabel("Books", fontsize=12)
    plt.ylabel("Status", fontsize=12)

    # 3. Save plot figure to image file
    plt.tight_layout()
    plt.savefig(output_filename, dpi=150)
    plt.close()

    print(f"Beginner bar chart saved successfully to '{output_filename}'")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner bar chart demonstration."""
    print("=== Beginner Level Bar Chart Demonstration ===")

    books = ["Data Science", "Biology", "Chemistry", "Python Tutorials", "Django Projects"]
    more_read = [12, 45, 73, 23, 42]

    generate_simple_bar_chart(books, more_read)
    return 0


if __name__ == "__main__":
    sys.exit(main())
