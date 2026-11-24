"""
Intermediate Level Bar Plot Customization Module (`intermediate_graph.py`).

This module provides functional plotting patterns designed for intermediate developers
(horizontal bar plots `barh`, direct data value annotations `bar_label`, grid styling).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import matplotlib`: Core Matplotlib plotting framework.
# - `import matplotlib.pyplot as plt`: State-based plotting interface.
# - `import sys`: System execution utilities.
# - `from typing import List, Tuple`: PEP 484 type hint generics.
# =========================================================================
import matplotlib
import sys
from typing import List, Tuple

# Ensure headless Agg backend for non-interactive execution
try:
    matplotlib.use("Agg")
except Exception:
    pass

import matplotlib.pyplot as plt


def generate_horizontal_bar_chart(
    categories: List[str],
    values: List[int],
    output_filename: str = "intermediate_horizontal_chart.png",
) -> None:
    """Generate a styled horizontal bar chart with data labels (`plt.barh`).

    Args:
        categories (List[str]): List of category strings.
        values (List[int]): Numerical value counts.
        output_filename (str): Image output filename.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Render horizontal bar chart (barh) with teal color palette
    bars = ax.barh(categories, values, color="#2b5c8f", edgecolor="#1d3e61")

    # Add data value labels on top of each bar
    ax.bar_label(bars, fmt="%d", padding=5, fontsize=10, fontweight="bold")

    ax.set_title("Developer Technology Popularity", fontsize=16, pad=15)
    ax.set_xlabel("Readership Count", fontsize=12)
    ax.set_ylabel("Technologies", fontsize=12)

    # Enable subtle background grid lines
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    ax.set_axisbelow(True)

    plt.tight_layout()
    fig.savefig(output_filename, dpi=200)
    plt.close(fig)

    print(f"Intermediate horizontal bar chart saved to '{output_filename}'")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate bar chart demonstration."""
    print("=== Intermediate Level Bar Chart Customization ===")

    experiences = [
        "Data Science",
        "Java",
        "PHP",
        "Python Tutorials",
        "Django FW",
        "JavaScript",
        "Flask",
    ]
    read_counts = [45, 10, 30, 75, 85, 55, 69]

    generate_horizontal_bar_chart(experiences, read_counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
