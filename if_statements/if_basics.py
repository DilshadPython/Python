"""Python Conditional Execution & Control Flow (If-Statement Module).

Import Notes & Architecture:
    - 'import sys': Provides access to system-specific parameters, interpreter settings, and memory footprint inspection.
    - 'from typing import Dict, List, Any, Union, Tuple, Optional': Enables PEP 484 type hint annotations for parameters and return types.
"""

import sys
from typing import Dict, List, Any, Union, Tuple, Optional

Number = Union[int, float]


def starter_if_examples() -> Dict[str, Any]:
    """Starter examples demonstrating basic Python conditional statements (if, if-else, if-elif-else).

    Conditional statements evaluate boolean expressions to control code execution flow.
    """
    # 1. Simple 'if' statement
    temperature = 25
    is_warm = False
    if temperature >= 20:
        is_warm = True

    # 2. Dual-branch 'if-else' statement
    user_age = 20
    access_granted = False
    if user_age >= 18:
        access_granted = True
    else:
        access_granted = False

    # 3. Multi-branch 'if-elif-else' grading evaluation
    score = 88
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # 4. Parity and Sign classification
    number = -7
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    return {
        "temperature": temperature,
        "is_warm": is_warm,
        "user_age": user_age,
        "access_granted": access_granted,
        "score": score,
        "assigned_grade": grade,
        "number": number,
        "number_sign": sign
    }


def logical_operators_and_short_circuit() -> Dict[str, Any]:
    """Demonstrates logical operators ('and', 'or', 'not') and short-circuit evaluation principles."""
    has_license = True
    has_insurance = True
    has_violations = False

    # 1. Logical 'and' operator
    can_drive = has_license and has_insurance

    # 2. Logical 'or' operator
    is_special_case = has_violations or has_license

    # 3. Logical 'not' operator (boolean inversion)
    is_clean_record = not has_violations

    # 4. Compound expression with operator precedence
    is_eligible = (has_license and has_insurance) and not has_violations

    # 5. Short-circuit evaluation demonstration
    eval_tracker: List[str] = []

    def evaluate_first() -> bool:
        eval_tracker.append("first")
        return False

    def evaluate_second() -> bool:
        eval_tracker.append("second")
        return True

    # In 'A and B', if A is False, B is NOT evaluated (short-circuit)
    and_result = evaluate_first() and evaluate_second()

    def evaluate_or_first() -> bool:
        eval_tracker.append("or_first")
        return True

    def evaluate_or_second() -> bool:
        eval_tracker.append("or_second")
        return False

    # In 'A or B', if A is True, B is NOT evaluated (short-circuit)
    or_result = evaluate_or_first() or evaluate_or_second()

    return {
        "can_drive": can_drive,
        "is_special_case": is_special_case,
        "is_clean_record": is_clean_record,
        "is_eligible": is_eligible,
        "short_circuit_eval_tracker": eval_tracker,
        "and_result": and_result,
        "or_result": or_result
    }


def truthiness_and_falsiness_evaluator(val: Any) -> Dict[str, Any]:
    """Evaluates the truth value (truthiness or falsiness) of any Python object inside a conditional statement."""
    # Standard Python truth value testing
    is_truthy = bool(val)

    category = "Truthy Object"
    if val is None:
        category = "NoneType (Falsy)"
    elif val == 0 or val == 0.0 or val == "":
        category = "Zero/Empty Primitive (Falsy)"
    elif isinstance(val, (list, tuple, dict, set)) and len(val) == 0:
        category = "Empty Container (Falsy)"
    elif not val:
        category = "Falsy Object"

    return {
        "evaluated_value": str(val),
        "is_truthy": is_truthy,
        "category": category,
        "bool_conversion": bool(val)
    }


def advanced_ternary_and_identity_checks(val: Any, sentinel: Optional[Any] = None) -> Dict[str, Any]:
    """Demonstrates inline ternary conditional expressions (x if condition else y) and Object Identity ('is') vs Value Equality ('==')."""
    # 1. Inline ternary conditional expression
    status = "Active" if isinstance(val, (int, str)) and val else "Inactive"

    # 2. Identity ('is') vs Equality ('==') comparison
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1

    value_equal = (list1 == list2)        # True: both contain identical elements [1, 2, 3]
    identity_equal = (list1 is list2)     # False: distinct memory objects
    alias_identity = (list1 is list3)     # True: both point to identical memory address

    # 3. Sentinel checking (Always use 'is' for None)
    is_sentinel_none = sentinel is None

    return {
        "ternary_status": status,
        "value_equality_check": value_equal,
        "identity_check_different_objs": identity_equal,
        "identity_check_same_ref": alias_identity,
        "is_sentinel_none": is_sentinel_none
    }


def pattern_matching_and_geometry(sides: Tuple[Number, Number, Number], command: str) -> Dict[str, Any]:
    """Demonstrates structural pattern matching concepts and geometry classification using conditional branching."""
    if not isinstance(sides, tuple) or len(sides) != 3:
        raise TypeError("sides must be a tuple of 3 numbers")
    if not isinstance(command, str):
        raise TypeError("command must be a string")

    a, b, c = sides

    # 1. Triangle Inequality Theorem Validation & Side Classification
    is_valid_triangle = (a + b > c) and (a + c > b) and (b + c > a)
    triangle_type = "Invalid Triangle"

    if is_valid_triangle:
        if a == b == c:
            triangle_type = "Equilateral"
        elif a == b or b == c or a == c:
            triangle_type = "Isosceles"
        else:
            triangle_type = "Scalene"

    # 2. Command Processor (simulating Pattern Matching match-case logic)
    action_result = "Unknown Action"
    cmd_lower = command.lower().strip()

    if cmd_lower in ("start", "run", "launch"):
        action_result = "System Initialized"
    elif cmd_lower in ("stop", "halt", "pause"):
        action_result = "System Suspended"
    elif cmd_lower in ("status", "info"):
        action_result = "System Running Smoothly"
    else:
        action_result = f"Fallback Action for '{command}'"

    return {
        "sides": sides,
        "is_valid_triangle": is_valid_triangle,
        "triangle_type": triangle_type,
        "command": command,
        "action_result": action_result
    }


def methods_and_attributes_in_conditionals(obj: Any, text: str, values: List[int]) -> Dict[str, Any]:
    """Demonstrates built-in methods, attributes, and aggregators evaluated inside conditional 'if' expressions.

    Key Methods & Attributes evaluated in conditions:
    1. Attribute & Type inspection: hasattr(), callable(), isinstance(), type()
    2. String predicate methods: .startswith(), .endswith(), .isdigit(), .isalpha()
    3. Iterable aggregators: any(), all()
    4. Interpreter attributes: sys.version_info
    """
    # 1. Attribute & Type Inspection inside conditions
    has_len = hasattr(obj, "__len__")
    is_function_callable = callable(obj)
    is_string_type = isinstance(obj, str)

    # 2. String predicate methods evaluated in conditions
    is_numeric_text = text.isdigit() if text else False
    starts_with_prefix = text.startswith(("https://", "http://")) if text else False

    # 3. Iterable aggregators (all / any) inside conditional blocks
    all_positive = all(v > 0 for v in values) if values else False
    has_even = any(v % 2 == 0 for v in values) if values else False

    # 4. System Version Attribute checking (sys.version_info)
    is_modern_python = sys.version_info >= (3, 10)

    return {
        "has_len_attribute": has_len,
        "is_function_callable": is_function_callable,
        "is_string_type": is_string_type,
        "is_numeric_text": is_numeric_text,
        "starts_with_prefix": starts_with_prefix,
        "all_positive": all_positive,
        "has_even": has_even,
        "is_modern_python": is_modern_python
    }
