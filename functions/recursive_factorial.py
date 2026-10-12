"""
Demonstrates recursive factorial calculation with step logging.
"""


def factorial_recur(n: int) -> int:
    """Return factorial of n computed recursively."""
    if n <= 1:
        return 1
    return n * factorial_recur(n - 1)


if __name__ == '__main__':
    print("Factorial of 5:", factorial_recur(5))
