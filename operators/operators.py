"""
Python Operators: Comprehensive Operator Demonstration Entrypoint.

This script demonstrates all major categories of Python operators:
- Arithmetic: +, -, *, /, //, %, **, @
- Assignment & Augmented Assignment: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=, :=
- Comparison / Relational: ==, !=, >, <, >=, <=
- Logical & Bitwise: and, or, not, &, |, ^, ~, <<, >>
- Identity & Membership: is, is not, in, not in
"""
# "import module" loads sys module.
import sys
# "from typing import ..." imports specific type hint symbols.
from typing import Dict, List, Tuple


def demonstrate_all_assignment_operators() -> Dict[str, float]:
    """
    Demonstrate basic and augmented assignment operators.

    Returns:
        Dict[str, float]: Mutated variable state values.
    """
    results: Dict[str, float] = {}

    # Basic assignment =
    x = 8.0
    results["assignment"] = x

    # Augmented arithmetic assignments
    x += 5   # x = x + 5 (13.0)
    results["add_assign"] = x

    x -= 3   # x = x - 3 (10.0)
    results["sub_assign"] = x

    x *= 2   # x = x * 2 (20.0)
    results["mul_assign"] = x

    x /= 4   # x = x / 4 (5.0)
    results["div_assign"] = x

    x %= 3   # x = x % 3 (2.0)
    results["mod_assign"] = x

    x //= 1  # x = x // 1 (2.0)
    results["floor_div_assign"] = x

    x **= 3  # x = x ** 3 (8.0)
    results["pow_assign"] = x

    # Walrus operator := assignment expression (Python 3.8+)
    if (walrus_val := x + 2) > 9:
        results["walrus_assign"] = walrus_val

    return results


def demonstrate_all_bitwise_assignment_operators() -> Dict[str, int]:
    """
    Demonstrate bitwise augmented assignment operators.

    Returns:
        Dict[str, int]: Mutated bitwise values.
    """
    results: Dict[str, int] = {}
    val = 16

    val &= 4   # 16 & 4 = 0
    results["and_assign"] = val

    val = 8
    val |= 4   # 8 | 4 = 12
    results["or_assign"] = val

    val ^= 4   # 12 ^ 4 = 8
    results["xor_assign"] = val

    val <<= 2  # 8 << 2 = 32
    results["left_shift_assign"] = val

    val >>= 3  # 32 >> 3 = 4
    results["right_shift_assign"] = val

    return results


if __name__ == "__main__":
    print("=== Python Operators Master Demonstration ===")
    assignment_res = demonstrate_all_assignment_operators()
    for op, val in assignment_res.items():
        print(f"  {op:<20}: {val}")

    print("\n=== Bitwise Assignment Operators ===")
    bitwise_res = demonstrate_all_bitwise_assignment_operators()
    for op, val in bitwise_res.items():
        print(f"  {op:<20}: {val}")
