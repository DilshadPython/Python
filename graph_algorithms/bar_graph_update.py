"""
Updated Technology Popularity Bar Chart Wrapper (`bar_graph_update.py`).

Fixed syntax error (`7481`) and variable reference mismatch ('experiens' -> 'categories').
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
    """Run updated bar chart plotting demonstration."""
    categories = [
        "Data Science",
        "Java",
        "PHP",
        "Python Tutorials",
        "Django FW",
        "JavaScript",
        "Flask",
    ]
    more_read = [45, 10, 30, 75, 85, 55, 69]

    render_bar_chart(
        categories=categories,
        values=more_read,
        title="Book Library",
        xlabel="Books",
        ylabel="Status",
        color="green",
        output_filename="bar_graph_update_output.png",
    )


if __name__ == "__main__":
    main()