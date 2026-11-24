"""
Demonstrates built-in min and max utility functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Sequence, Tuple, TypeVar

T = TypeVar("T", int, float)


def get_max_and_min(numbers: Sequence[T]) -> Tuple[T, T]:
    """Return a tuple containing maximum and minimum values from a sequence."""
    if not numbers:
        raise ValueError("Sequence cannot be empty")
    return max(numbers), min(numbers)


if __name__ == "__main__":
    data = [12, 45, 2, 89, 34]
    max_val, min_val = get_max_and_min(data)
    print(f"Max: {max_val}, Min: {min_val}")
