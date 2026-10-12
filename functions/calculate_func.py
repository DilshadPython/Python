"""
Demonstrates returning multiple arithmetic calculation results as a tuple.
"""
# Import explanation:
# 'from typing import Tuple' imports Tuple from typing to annotate fixed-length returned tuples.
from typing import Tuple


def calculate(a: float, b: float) -> Tuple[float, float, float, float]:
    """Perform addition, subtraction, multiplication, and safe division."""
    div_result = a / b if b != 0 else float("nan")
    return a + b, a - b, a * b, div_result


if __name__ == "__main__":
    add_res, sub_res, mul_res, div_res = calculate(10, 2)
    print(f"Add: {add_res}, Sub: {sub_res}, Mul: {mul_res}, Div: {div_res}")
