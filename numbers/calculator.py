"""
Simple Calculator Module (Python 3.3 to Python 3.13 Compatible)

Supported operations: +, -, *, /, ^ (exponent), %, // (floor division)

Python Version Notes:
- Python 3.3 - 3.13: `/` always performs true float division (e.g. 5 / 2 == 2.5).
- Python 2.7 Comparison: `/` performed integer truncation unless float inputs or
  `from __future__ import division` was used. `input()` evaluated input as code.
"""

from __future__ import print_function, division
import sys

# Cross-version input compatibility shim
try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def calculate(num1, op, num2):
    """
    Executes calculation for num1 and num2 given operator op.
    Returns calculated numeric result.
    Raises ValueError for unknown operators or ZeroDivisionError for division by zero.
    """
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif op == '^':
        return num1 ** num2
    elif op == '%':
        if num2 == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")
        return num1 % num2
    elif op == '//':
        if num2 == 0:
            raise ZeroDivisionError("Cannot floor divide by zero.")
        return num1 // num2
    else:
        raise ValueError("Unsupported operator: {}".format(op))


def main():
    """Interactive CLI execution."""
    print("Small calculation operators: +, -, *, /, ^ (exponent), %, // (floor division)")
    try:
        n1_str = get_input("Enter num1: ")
        op = get_input("Enter op: ").strip()
        n2_str = get_input("Enter num2: ")
        
        num1 = float(n1_str) if '.' in n1_str else int(n1_str)
        num2 = float(n2_str) if '.' in n2_str else int(n2_str)
        
        res = calculate(num1, op, num2)
        print("Result: {}".format(res))
    except Exception as err:
        print("Error: {}".format(err))


if __name__ == '__main__':
    main()

