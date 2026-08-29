"""
Demonstrates basic calculator operations returned as a dictionary.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Dict, Union


def calculator(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    """Return dictionary containing sum, subtraction, multiplication, and division."""
    return {
        'add': a + b,
        'sub': a - b,
        'mul': a * b,
        'div': a / b if b != 0 else float('nan')
    }


if __name__ == '__main__':
    res = calculator(20, 5)
    print("Basic calculator results:", res)
