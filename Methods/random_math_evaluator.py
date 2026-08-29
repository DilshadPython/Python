"""
Demonstrates combining random value generation with function calculations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
import random
from typing import Tuple


def generate_random_number(min_val: int = 0, max_val: int = 100) -> int:
    """Generate a random integer within inclusive range [min_val, max_val]."""
    return random.randint(min_val, max_val)


def evaluate_math_operations(x: int, y: int) -> Tuple[int, int, int, int, int, float]:
    """
    Perform core math operations on x and y: sum, diff, prod, floor_div, mod, div.
    
    Args:
        x (int): Left integer operand.
        y (int): Right integer operand (must be non-zero).
        
    Returns:
        Tuple[int, int, int, int, int, float]: Results tuple.
    """
    safe_y: int = y if y != 0 else 1
    a: int = x + safe_y
    b: int = x - safe_y
    c: int = x * safe_y
    d: int = x // safe_y
    e: int = x % safe_y
    f: float = x / safe_y
    return a, b, c, d, e, f


if __name__ == '__main__':
    val1 = generate_random_number(1, 50)
    val2 = generate_random_number(1, 50)
    results = evaluate_math_operations(val1, val2)
    print(f"Inputs: x={val1}, y={val2}")
    print("Results (add, sub, mul, floor_div, mod, div):", results)
