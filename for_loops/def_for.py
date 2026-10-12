"""Basic Function Execution with 'for' Loop Range Iteration.

Demonstrates defining a modular function that uses a 'for' loop to iterate
through a numerical range.

Import Notes:
    - 'from typing import List': Standard library typing import for list return type annotations.
"""

from typing import List


def generate_range_list(start: int = 1, stop: int = 10) -> List[int]:
    """Generate and return a list of integers from start to stop inclusive."""
    numbers: List[int] = []
    # range(start, stop + 1) generates numbers from start up to stop
    for i in range(start, stop + 1):
        numbers.append(i)
        print(f"Iteration value: {i}")
    return numbers


def demo_def_for() -> None:
    """Execute range iteration demonstration function."""
    print("--- Running Basic Function 'for' Loop ---")
    result_list = generate_range_list(1, 10)
    print(f"Generated Range List: {result_list}")


if __name__ == "__main__":
    demo_def_for()
