"""
Demonstrates functions returning boolean truth values.
"""


def is_even_boolean(n: int) -> bool:
    """Return True if integer n is even, False otherwise."""
    return n % 2 == 0


def is_positive(n: int) -> bool:
    """Return True if number n is positive, False otherwise."""
    return n > 0


if __name__ == '__main__':
    print("is_even_boolean(10):", is_even_boolean(10))
    print("is_positive(5):", is_positive(5))
