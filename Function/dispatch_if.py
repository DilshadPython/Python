"""
Demonstrates conditional branching (if/elif/else) for function dispatching.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Optional, Union


def dispatch_if(operator: str, x: Union[int, float], y: Union[int, float]) -> Optional[Union[int, float]]:
    """Perform operation matching `operator` string using if-elif-else logic."""
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y if y != 0 else float('nan')
    elif operator == 'rem':
        return x % y if y != 0 else float('nan')
    else:
        return None


if __name__ == '__main__':
    print("Operators: ['add', 'sub', 'mul', 'div', 'rem']")
    op = input('Enter operator: ').strip()
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        res = dispatch_if(op, a, b)
        print(f"Result: {res}")
    except ValueError:
        print("Invalid input")
