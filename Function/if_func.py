"""
Demonstrates helper predicate functions used inside conditional statements.
"""

def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

def check_number_parity(num: int) -> str:
    """Return descriptive string indicating whether number is even or odd."""
    return 'Even number' if is_even(num) else 'This is odd number'

if __name__ == '__main__':
    print("4 is:", check_number_parity(4))
    print("7 is:", check_number_parity(7))
