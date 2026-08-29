"""
Demonstrates safe handling of negative values in recursive factorial computations.
"""


def factorial_recur(n: int) -> int:
    """Return factorial of n, raising ValueError for negative numbers."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recur(n - 1)


if __name__ == '__main__':
    print("Factorial 5:", factorial_recur(5))
