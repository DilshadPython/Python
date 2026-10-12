"""
Nearest Number & Number Formatting (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: `round()` uses Banker's Rounding (round-half-to-even).
  Example: round(2.5) -> 2, round(3.5) -> 4. Returns integer when ndigits is None.
- Python 2.7 Comparison: `round()` rounded half away from zero (round(2.5) -> 3.0)
  and always returned a float.
- Formatting: `"{:,}".format(val)` and `"{:.2f}".format(val)` work across all versions.
"""

from __future__ import print_function, division

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def format_and_round(num1, num2):
    """
    Performs addition and division formatting/rounding operations.
    Returns a dictionary of structured results.
    """
    sum_val = num1 + num2
    div_val = (num1 / num2) if num2 != 0 else float('inf')

    rounded_sum = round(sum_val)
    rounded_div = round(div_val)
    rounded_div_2dec = round(div_val, 2)

    return {
        "num1": num1,
        "num2": num2,
        "sum": sum_val,
        "division": div_val,
        "rounded_sum": rounded_sum,
        "rounded_sum_formatted": "{:,}".format(rounded_sum),
        "rounded_div": rounded_div,
        "sum_2dec": "{:.2f}".format(sum_val),
        "rounded_div_2dec": rounded_div_2dec
    }


def main():
    """Interactive execution for rounding & formatting demonstration."""
    try:
        n1_str = get_input('Enter num1: ')  # e.g., 888
        n2_str = get_input('Enter num2: ')  # e.g., 112
        n1 = float(n1_str)
        n2 = float(n2_str)
    except (ValueError, TypeError):
        n1, n2 = 888.0, 112.0
        print("Using default values (888.0, 112.0):")

    res = format_and_round(n1, n2)
    print("Rounded Sum:", res["rounded_sum"])
    print("Formatted Sum with Commas:", res["rounded_sum_formatted"])
    print("Rounded Division:", res["rounded_div"])
    print("Sum with 2 Decimals:", res["sum_2dec"])
    print("Rounded Division (2 decimals):", res["rounded_div_2dec"])


if __name__ == '__main__':
    main()