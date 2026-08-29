"""
Demonstrates factorial mathematical definition implemented recursively.
"""


def factorial_recur(n: int) -> int:
    """Return factorial of non-negative integer n using recursive base case."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recur(n - 1)


if __name__ == '__main__':
    print("Recursive factorial 5:", factorial_recur(5))
