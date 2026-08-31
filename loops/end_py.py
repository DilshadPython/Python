"""Customizing Line Endings in Python 'print()' Function.

Demonstrates using the 'end' parameter of the built-in print() function
to override the default newline character ('\n') with custom string delimiters
(such as commas, spaces, or custom symbols) during loop iteration.

Import Notes:
    - 'from typing import List': Standard library typing module import used to provide
      explicit type annotations for functions returning list data structures.
"""

from typing import List


def format_horizontal_sequence(limit: int = 16, delimiter: str = ", ") -> str:
    """Format a sequence of numbers into a single delimiter-separated string.

    Args:
        limit: Upper range limit (exclusive, default: 16).
        delimiter: Separator string appended after each number (default: ", ").

    Returns:
        Formatted horizontal sequence string.
    """
    elements = [str(i) for i in range(limit)]
    result = delimiter.join(elements)
    print(result)
    return result


def demonstrate_print_end_parameter() -> List[str]:
    """Execute demonstration of custom 'end' parameter behavior in print().

    Returns:
        List of formatted output strings produced by the print end examples.
    """
    outputs: List[str] = []

    # 1. Custom comma delimiter in range loop
    line1 = format_horizontal_sequence(16, ", ")
    outputs.append(line1)

    print("\n=======================\n")

    # 2. Default newline print vs custom space ending
    print("Welcome to")
    print("Python")

    print("Hi", end=" ")
    print("JavaScript\n")
    outputs.append("Hi JavaScript")

    # 3. Custom '&' delimiter loop
    line2 = format_horizontal_sequence(10, " & ")
    outputs.append(line2)

    return outputs


def demo_end_py() -> None:
    """Run demonstration of print() end parameter customization."""
    print("--- Customizing print() 'end' Parameter ---")
    demonstrate_print_end_parameter()


if __name__ == "__main__":
    demo_end_py()