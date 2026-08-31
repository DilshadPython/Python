"""
Demonstrates interactive arithmetic calculator operations inside a while loop.
"""
from typing import Union


def calculate_operation(var1: float, var2: float, op: str) -> Union[float, str]:
    """Execute arithmetic operation between two numbers based on operator string."""
    if op == '+':
        return var1 + var2
    elif op == '-':
        return var1 - var2
    elif op == '*':
        return var1 * var2
    elif op == '/':
        return var1 / var2 if var2 != 0 else "Error: Division by zero"
    else:
        return "Error: Unrecognized operator"


if __name__ == '__main__':
    result = calculate_operation(10.0, 5.0, '+')
    print(f"10.0 + 5.0 = {result}")
