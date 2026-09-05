"""
Fibonacci Algorithms: Object-Oriented Iterator Class

This module demonstrates implementing a custom Python iterator class for generating
Fibonacci numbers by overloading the `__iter__` and `__next__` magic dunder methods.

Magic Methods:
- `__iter__(self)`: Returns the iterator object instance (`self`).
- `__next__(self)`: Calculates and returns the next term in sequence, or raises `StopIteration`.
"""
from typing import Iterator


class FibonacciIterator:
    """An iterable object producing Fibonacci terms up to a maximum count."""

    def __init__(self, limit: int) -> None:
        if limit < 0:
            raise ValueError("Limit cannot be negative.")
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self) -> Iterator[int]:
        """Returns the iterator instance itself."""
        return self

    def __next__(self) -> int:
        """Returns the next Fibonacci number or raises StopIteration when limit is reached."""
        if self.count >= self.limit:
            raise StopIteration

        res = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return res


def main() -> None:
    """Demonstrates custom Fibonacci iterator class usage."""
    print("=" * 60)
    print("6. Object-Oriented Fibonacci Iterator (`__iter__` & `__next__`)")
    print("=" * 60)

    limit = 12
    fib_iter = FibonacciIterator(limit)

    print(f"\nIterating over `FibonacciIterator({limit})` instance:")
    for term in fib_iter:
        print(f"  {term}", end=" ")
    print()


if __name__ == "__main__":
    main()
