"""String Repetition and Line Formatting with Python 'print()'.

Demonstrates string multiplication operators combined with escape sequences
('\\t', '\\n') and the 'end' argument of print().

Import Notes:
    - 'from typing import Tuple': Standard library typing import for tuple return type hints.
"""

from typing import Tuple


def repeat_string_horizontal(text: str = "Hello", count: int = 5) -> str:
    """Repeat text string horizontally with tab delimiters.

    Args:
        text: Target text to repeat.
        count: Number of repetitions.

    Returns:
        The formatted repeated horizontal string.
    """
    formatted = (text + "\t") * count
    print(formatted)
    return formatted


def repeat_string_vertical(text: str = "Hello", count: int = 3) -> str:
    """Repeat text string vertically with newline delimiters.

    Args:
        text: Target text to repeat.
        count: Number of repetitions.

    Returns:
        The formatted repeated vertical string.
    """
    formatted = (text + "\n") * count
    print(formatted, end="")
    return formatted


def demo_for_print() -> Tuple[str, str]:
    """Run demonstration of string repetition formatting."""
    print("--- 1. Horizontal Tab Repetition ---")
    h_res = repeat_string_horizontal("Hello", 5)

    print("--- 2. Vertical Newline Repetition ---")
    v_res = repeat_string_vertical("Hello", 3)

    return h_res, v_res


if __name__ == "__main__":
    demo_for_print()