"""
Demonstrates helper predicate functions used inside conditional statements.
"""


def is_even_number(n: int) -> bool:
    """Return True if integer n is even, False otherwise."""
    return n % 2 == 0


def check_number_parity(num: int) -> str:
    """Evaluate and return parity status string for a given integer."""
    if is_even_number(num):
        return f"The number {num} is even."
    else:
        return f"The number {num} is odd."


if __name__ == '__main__':
    print(check_number_parity(7))
    print(check_number_parity(12))
