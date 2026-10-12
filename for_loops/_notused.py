"""Demonstration of Unused Loop Variables ('_') in Python.

In Python, the single underscore '_' is conventionally used as a placeholder
for a loop variable when the loop counter or current item is intentionally not
referenced inside the loop body.

Import Notes:
    - 'from typing import List': Standard library typing module import used to provide
      explicit type annotations for functions returning list data structures.
"""

from typing import List


def execute_unused_variable_loop(repetitions: int = 5) -> List[str]:
    """Execute a loop using '_' as an intentional throwaway loop variable.

    Args:
        repetitions: Number of times to execute the loop block (default: 5).

    Returns:
        List of formatted execution strings generated during iteration.
    """
    output_messages: List[str] = []
    # '_' indicates the loop variable is intentionally ignored
    for _ in range(repetitions):
        msg = "The '_' variable is an intentional throwaway variable."
        output_messages.append(msg)
        print(msg)
    return output_messages


def demo_not_used() -> None:
    """Run demonstration of unused loop variable idiom."""
    print("--- Demonstrating Throwaway Loop Variable '_' ---")
    execute_unused_variable_loop(3)


if __name__ == "__main__":
    demo_not_used()