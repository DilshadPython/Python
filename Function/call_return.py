"""
Demonstrates function calls, return values, and mathematical exponents.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def square(n: Union[int, float]) -> Union[int, float]:
    """Calculate square of a number."""
    return n * n


def power(n: Union[int, float], exp: int = 3) -> Union[int, float]:
    """Calculate nth power of a number."""
    return n ** exp


def main() -> None:
    """Execute main interactive workflow."""
    try:
        num = int(input('Enter a number: '))
        print(f'The square of num: {square(num)}')
        num1 = int(input('Enter second number: '))
        print(f'The power of second number: {power(num1)}')
        num2 = int(input('Enter third number: '))
        print(f'The power of num2: {power(num2)}')
    except ValueError:
        print("Invalid number input")


if __name__ == '__main__':
    main()
