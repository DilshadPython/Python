"""Numeric Sequence Generation with 'range()' in Python.

Demonstrates range(stop), range(start, stop), and range(start, stop, step)
sequence generation for loop iteration. Corrects comment spelling.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing imports for list and tuple type hints.
"""

from typing import List, Tuple


def generate_single_arg_range(stop: int = 10) -> List[int]:
    """Generate sequence from 0 up to stop (exclusive)."""
    numbers: List[int] = []
    print(f"--- range({stop}) ---")
    for num in range(stop):
        numbers.append(num)
        print(num)
    return numbers


def generate_two_arg_range(start: int = 1, stop: int = 21) -> List[int]:
    """Generate sequence from start up to stop (exclusive)."""
    numbers: List[int] = []
    print(f"\n--- range({start}, {stop}) ---")
    for num in range(start, stop):
        numbers.append(num)
        print(num, end=" ")
    print()
    return numbers


def generate_stepped_range(start: int, stop: int, step: int) -> List[int]:
    """Generate sequence from start up to stop using a step increment."""
    numbers: List[int] = []
    print(f"\n--- range({start}, {stop}, {step}) ---")
    for num in range(start, stop, step):
        numbers.append(num)
        print(num, end=" ")
    print()
    return numbers


def demo_for_range() -> Tuple[List[int], List[int], List[int], List[int]]:
    """Run range sequence generation demonstration."""
    r1 = generate_single_arg_range(10)
    r2 = generate_two_arg_range(1, 21)
    r3 = generate_stepped_range(1, 21, 3)

    # Corrected spelling: 'tweice' -> 'twice' (step by 2)
    r4 = generate_stepped_range(1, 24, 2)

    return r1, r2, r3, r4


if __name__ == "__main__":
    demo_for_range()
