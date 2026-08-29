"""
Demonstrates recursive factorial calculation with input validation.
"""


def factorial_recur(n: int) -> int:
    """Return recursive factorial result with validation."""
    if n <= 1:
        return 1
    return n * factorial_recur(n - 1)


if __name__ == '__main__':
    print("Factorial 5:", factorial_recur(5))
