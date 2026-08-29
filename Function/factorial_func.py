"""
Demonstrates iterative factorial computation.
"""


def factorial(number: int) -> int:
    """Compute factorial of non-negative integer `number` using an iterative loop."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


if __name__ == '__main__':
    try:
        num = int(input('Enter a number: '))
        print(f"{num}! = {factorial(num)}")
    except ValueError:
        print("Invalid number input")
