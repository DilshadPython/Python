"""
Python Operators: Comparison, Identity, & Membership Operators Module.

This module demonstrates:
- Relational / Comparison: ==, !=, >, <, >=, <=
- Identity Operators: is, is not (evaluating object memory address / id())
- Membership Operators: in, not in (evaluating element containment in sequences)
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Any, List, Tuple


def evaluate_comparison_operators(x: float, y: float) -> Tuple[bool, bool, bool, bool, bool, bool]:
    """
    Evaluate all 6 relational comparison operators between two numbers.

    Args:
        x (float): Left operand.
        y (float): Right operand.

    Returns:
        Tuple[bool, ...]: Results of (==, !=, >, <, >=, <=).
    """
    eq = (x == y)
    ne = (x != y)
    gt = (x > y)
    lt = (x < y)
    ge = (x >= y)
    le = (x <= y)

    return eq, ne, gt, lt, ge, le


def evaluate_identity_operators(obj_a: Any, obj_b: Any, obj_c: Any) -> Tuple[bool, bool, bool]:
    """
    Evaluate object identity operators (is, is not) comparing object memory references (id()).

    Args:
        obj_a (Any): First object.
        obj_b (Any): Second object (alias of obj_a).
        obj_c (Any): Third object (separate instance with identical content).

    Returns:
        Tuple[bool, bool, bool]: (a is b, a is obj_c, a is not obj_c).
    """
    is_alias = (obj_a is obj_b)
    is_same_instance = (obj_a is obj_c)
    is_not_same_instance = (obj_a is not obj_c)

    return is_alias, is_same_instance, is_not_same_instance


def evaluate_membership_operators(target_element: Any, sequence: List[Any]) -> Tuple[bool, bool]:
    """
    Evaluate sequence membership operators (in, not in).

    Args:
        target_element (Any): Item to search for.
        sequence (List[Any]): Container sequence (list, tuple, set, dict).

    Returns:
        Tuple[bool, bool]: (target in sequence, target not in sequence).
    """
    is_present = target_element in sequence
    is_absent = target_element not in sequence

    return is_present, is_absent
