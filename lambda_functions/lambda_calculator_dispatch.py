"""
Demonstrates a dictionary dispatch table populated with lambda functions for arithmetic operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Dict, Union

# Numeric type hint alias
Numeric = Union[int, float]

# Calculator dispatch dictionary mapping operator strings to lambda functions
CALCULATOR_OPS: Dict[str, Callable[[Numeric, Numeric], Numeric]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b if b != 0 else float('nan'),
    '%': lambda a, b: a % b if b != 0 else 0,
    '*': lambda a, b: a * b,
    '**': lambda a, b: a ** b,
}


def calculate_operation(a: Numeric, b: Numeric, op: str) -> Numeric:
    """
    Execute arithmetic operation on a and b using the lambda dispatch table.
    
    Args:
        a (Numeric): Left operand.
        b (Numeric): Right operand.
        op (str): Operator key string ('+', '-', '/', '%', '*', '**').
        
    Returns:
        Numeric: Calculated result.
        
    Raises:
        KeyError: If op string is not in CALCULATOR_OPS dictionary.
    """
    if op not in CALCULATOR_OPS:
        raise KeyError(f"Unsupported operator '{op}'. Supported: {list(CALCULATOR_OPS.keys())}")
    return CALCULATOR_OPS[op](a, b)


if __name__ == '__main__':
    print("7 + 9 =", calculate_operation(7, 9, '+'))
    print("7 - 9 =", calculate_operation(7, 9, '-'))
    print("7 / 9 =", calculate_operation(7, 9, '/'))
    print("7 % 9 =", calculate_operation(7, 9, '%'))
    print("7 * 9 =", calculate_operation(7, 9, '*'))
    print("7 ** 9 =", calculate_operation(7, 9, '**'))
