"""
Demonstrates encapsulated arithmetic calculator returning dictionary results.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Dict, Union


def calculator(a: Union[int, float] = 17, b: Union[int, float] = 36) -> Dict[str, Union[int, float]]:
    """Return arithmetic operation results for a and b in a dictionary."""
    return {
        'add': a + b,
        'sub': a - b,
        'mul': a * b,
        'div': a / b if b != 0 else float('nan'),
        'rem': a % b if b != 0 else float('nan')
    }


if __name__ == '__main__':
    results = calculator(17, 36)
    print("Calculator results:", results)
