"""
Demonstrates dictionary dispatch table pattern to emulate switch/case statements.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Dict, Optional, Union


def dispatch_dict(operator: str, x: Union[int, float], y: Union[int, float]) -> Optional[Union[int, float]]:
    """Dispatch arithmetic operations using a dictionary mapping."""
    operations: Dict[str, Callable[[], Union[int, float]]] = {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y if y != 0 else float('nan'),
        'rem': lambda: x % y if y != 0 else float('nan'),
    }
    action = operations.get(operator)
    return action() if action else None


if __name__ == '__main__':
    print("Operators: ['add', 'sub', 'mul', 'div', 'rem']")
    op = input('Select an operator: ').strip()
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        res = dispatch_dict(op, a, b)
        print(f"Result: {res}")
    except ValueError:
        print("Invalid numeric input")
