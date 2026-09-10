"""
Book Library Read Status Bar Chart Wrapper (`bar_graph.py`).

This module renders a vertical bar plot comparing readership status across book categories.
Corrected spelling ("Chimiches" -> "Chemistry").
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from bar_chart_generator import render_bar_chart`: Modular plot renderer.
# =========================================================================
try:
    from graph_algorithms.bar_chart_generator import render_bar_chart
except ImportError:
    from bar_chart_generator import render_bar_chart


def main() -> None:
    """Run bar chart plotting demonstration."""
    books = ["Data Science", "Biology", "Chemistry", "Python Tutorials", "Django Projects"]
    more_read = [12, 45, 73, 23, 42]

    render_bar_chart(
        categories=books,
        values=more_read,
        title="Book Library",
        xlabel="Books",
        ylabel="Status",
        color="green",
        output_filename="bar_graph_output.png",
    )


if __name__ == "__main__":
    main()