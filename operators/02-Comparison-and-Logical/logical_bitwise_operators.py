"""
Python Operators: Logical & Bitwise Operators Module.

This module demonstrates:
- Boolean Logical Operators: and, or, not (with short-circuit evaluation)
- Bitwise Operators: & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Dict, Tuple


def demonstrate_logical_operators(condition_a: bool, condition_b: bool) -> Tuple[bool, bool, bool, bool]:
    """
    Demonstrate logical boolean operators (and, or, not).

    Args:
        condition_a (bool): First boolean state.
        condition_b (bool): Second boolean state.

    Returns:
        Tuple[bool, bool, bool, bool]: (a and b, a or b, not a, not b).
    """
    and_result = condition_a and condition_b
    or_result = condition_a or condition_b
    not_a = not condition_a
    not_b = not condition_b

    return and_result, or_result, not_a, not_b


def demonstrate_short_circuit_evaluation(call_tracker: Dict[str, bool], trigger_second: bool) -> bool:
    """
    Demonstrate boolean short-circuit evaluation for 'or' and 'and' operators.

    Args:
        call_tracker (Dict[str, bool]): Dictionary tracking function invocation side-effects.
        trigger_second (bool): Controls whether second operand function is executed.

    Returns:
        bool: Evaluated logical boolean result.
    """
    def first_func() -> bool:
        call_tracker["first_func_called"] = True
        return True

    def second_func() -> bool:
        call_tracker["second_func_called"] = True
        return trigger_second

    # Short-circuit OR: Since first_func() returns True, second_func() is NEVER evaluated
    return first_func() or second_func()


def demonstrate_bitwise_operators(x: int, y: int) -> Tuple[int, int, int, int, int, int]:
    """
    Demonstrate binary bitwise operations on integers.

    Args:
        x (int): Left integer operand.
        y (int): Right integer operand.

    Returns:
        Tuple[int, ...]: Results of (x & y, x | y, x ^ y, ~x, x << 2, y >> 1).
    """
    bit_and = x & y       # Bitwise AND
    bit_or = x | y        # Bitwise OR
    bit_xor = x ^ y       # Bitwise XOR
    bit_not = ~x          # Bitwise NOT (Two's complement ~x = -x - 1)
    shift_left = x << 2   # Left shift multiplies by 2^2 = 4
    shift_right = y >> 1  # Right shift divides by 2^1 = 2

    return bit_and, bit_or, bit_xor, bit_not, shift_left, shift_right
