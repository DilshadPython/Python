"""Return Statement Mechanics & Best Practices Tutorial Module.

This module provides a production-grade, PEP 8-compliant implementation
demonstrating the mechanics, design patterns, and cross-version evolution of the
`return` statement in Python. It covers implicit vs explicit None returns, multiple
value tuple packing, higher-order function closures, try-finally override behaviors,
generator return values (PEP 380), guard clause patterns, and dir() introspection.
"""

import datetime
import sys
from typing import Any, Callable, Dict, Generator, List, NoReturn, Optional, Tuple, Union


# =============================================================================
# 1. STARTER RETURN EXAMPLES & FUNDAMENTALS
# =============================================================================

def calculate_triangle_volume(base_area: float, height: float) -> None:
    """Demonstrate a function without an explicit return statement.

    In Python, if execution reaches the end of a function without encountering
    an explicit `return`, CPython automatically returns `None`.

    Args:
        base_area: Base area of the triangle pyramid.
        height: Height of the triangle pyramid.
    """
    _volume = (1 / 3) * base_area * height
    # Implicit return None occurs at end of function execution


def calculate_cube_volume(length: float, width: float, height: float) -> float:
    """Calculate and return the volume of a rectangular prism.

    Args:
        length: Length of the prism.
        width: Width of the prism.
        height: Height of the prism.

    Returns:
        The calculated volume as a float.
    """
    return float(length * width * height)


def explicit_none_return(condition: bool) -> Optional[str]:
    """Demonstrate explicit return statement with optional string payload.

    Args:
        condition: Execution control flag.

    Returns:
        A success string if condition is True, else explicit None.
    """
    if condition:
        return "Condition satisfied"
    return None


def get_coordinate_3d(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """Demonstrate returning multiple values via tuple packing.

    In Python, comma-separated values in a `return` statement are automatically
    packed into an immutable tuple object.

    Args:
        x: X-axis coordinate.
        y: Y-axis coordinate.
        z: Z-axis coordinate.

    Returns:
        A tuple of (x, y, z).
    """
    return x, y, z


def check_even_odd(number: int) -> str:
    """Demonstrate early return branching based on modulo checking.

    Args:
        number: Integer value to evaluate.

    Returns:
        'Even' if number % 2 == 0, else 'Odd'.
    """
    if not isinstance(number, int):
        raise TypeError("Input 'number' must be an integer")
    if number % 2 == 0:
        return "Even"
    return "Odd"


def starter_return_examples() -> Dict[str, Any]:
    """Aggregates starter return demonstrations into a structured dictionary.

    Returns:
        Structured dictionary containing implicit None, explicit calculations,
        tuple packing/unpacking, and conditional early returns.
    """
    tri_res = calculate_triangle_volume(7.0, 8.0)
    cube_val = calculate_cube_volume(7.0, 8.0, 4.0)
    explicit_true = explicit_none_return(True)
    explicit_false = explicit_none_return(False)
    
    coords = get_coordinate_3d(7.0, 8.0, 4.0)
    pos_x, pos_y, pos_z = coords

    even_test = check_even_odd(42)
    odd_test = check_even_odd(7)

    return {
        "implicit_none_result": tri_res,
        "implicit_none_type": type(tri_res).__name__,
        "cube_volume": cube_val,
        "explicit_none_true": explicit_true,
        "explicit_none_false": explicit_false,
        "returned_tuple": coords,
        "unpacked_coords": {"x": pos_x, "y": pos_y, "z": pos_z},
        "even_check": even_test,
        "odd_check": odd_test,
    }


# =============================================================================
# 2. ADVANCED RETURN MECHANICS & HIGHER-ORDER CLOSURES
# =============================================================================

def create_multiplier(factor: float) -> Callable[[float], float]:
    """Demonstrate returning a callable function (closure) with state binding.

    Args:
        factor: Multiplier scalar to bind in outer scope.

    Returns:
        A inner function `multiplier` expecting a single float argument.
    """
    def multiplier(number: float) -> float:
        return number * factor

    return multiplier


def execute_finally_return_demo(override: bool) -> str:
    """Demonstrate return statement interactions inside try...finally blocks.

    IMPORTANT: A return statement inside a `finally` block overrides any
    return statement or uncaught exception raised within the `try` block.

    Args:
        override: If True, executes a return in the finally block.

    Returns:
        A string indicating which return statement prevailed.
    """
    try:
        return "Return from try block"
    finally:
        if override:
            return "Return overridden by finally block"


def generator_with_return_value(limit: int) -> Generator[int, None, str]:
    """Demonstrate return statement inside a generator function (PEP 380).

    In Python 3.3+, generator functions can include a `return value` statement.
    The returned value is attached to `StopIteration.value` upon completion.

    Args:
        limit: Iteration threshold.

    Yields:
        Integers from 0 up to limit - 1.

    Returns:
        Summary string payload on iteration termination.
    """
    for i in range(limit):
        yield i
    return f"Completed generator iteration up to {limit}"


def consume_generator(limit: int) -> Tuple[List[int], str]:
    """Helper function to consume a generator and extract its return payload.

    Args:
        limit: Generator count limit.

    Returns:
        Tuple of (list of yielded items, generator return value string).
    """
    gen = generator_with_return_value(limit)
    items: List[int] = []
    return_val = ""
    while True:
        try:
            items.append(next(gen))
        except StopIteration as exc:
            return_val = str(exc.value)
            break
    return items, return_val


def raise_fatal_error(message: str) -> NoReturn:
    """Demonstrate typing.NoReturn for functions that never return control.

    Args:
        message: Exception message.

    Raises:
        RuntimeError: Always raised to illustrate NoReturn semantics.
    """
    raise RuntimeError(f"Fatal error encountered: {message}")


def advanced_return_mechanics(limit: int = 4, override_finally: bool = True) -> Dict[str, Any]:
    """Aggregates advanced return mechanics into a structured dictionary.

    Returns:
        Dictionary containing closure evaluation, try-finally override outputs,
        generator StopIteration payloads, and NoReturn exception handling.
    """
    double_fn = create_multiplier(2.0)
    triple_fn = create_multiplier(3.0)
    
    double_val = double_fn(7.0)
    triple_val = triple_fn(7.0)

    try_normal = execute_finally_return_demo(override=False)
    try_override = execute_finally_return_demo(override=override_finally)

    yielded_items, gen_return_payload = consume_generator(limit)

    no_return_caught = False
    error_msg = ""
    try:
        raise_fatal_error("System resource unavailable")
    except RuntimeError as err:
        no_return_caught = True
        error_msg = str(err)

    return {
        "double_7": double_val,
        "triple_7": triple_val,
        "try_normal_return": try_normal,
        "try_override_return": try_override,
        "generator_yielded_items": yielded_items,
        "generator_stop_iteration_value": gen_return_payload,
        "no_return_exception_caught": no_return_caught,
        "no_return_error_message": error_msg,
    }


# =============================================================================
# 3. GUARD CLAUSES & INTROSPECTION PATTERNS
# =============================================================================

def validate_and_process_user(data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Demonstrate the Guard Clause (Early Return) pattern.

    Replaces deeply nested `if/else` ladders with early exit checks, leaving
    the primary execution logic at root indentation level.

    Args:
        data: User data dictionary or None.

    Returns:
        Structured result payload with status flag and message.
    """
    # Guard 1: Null check
    if data is None:
        return {"status": "error", "message": "Input data cannot be None"}

    # Guard 2: Type validation
    if not isinstance(data, dict):
        return {"status": "error", "message": "Input data must be a dictionary"}

    # Guard 3: Required field check
    if "username" not in data or not data["username"]:
        return {"status": "error", "message": "Missing required field: username"}

    # Guard 4: Business constraint check
    age = data.get("age", 0)
    if not isinstance(age, (int, float)) or age < 18:
        return {"status": "error", "message": "User must be at least 18 years old"}

    # Happy path execution (unindented)
    normalized_username = str(data["username"]).strip().lower()
    return {
        "status": "success",
        "message": "User processed successfully",
        "processed_data": {
            "username": normalized_username,
            "age": int(age),
            "is_active": True,
        },
    }


def inspect_return_object(obj: Any) -> List[str]:
    """Demonstrate dir() introspection on function return values.

    Args:
        obj: Any returned Python object.

    Returns:
        Sorted list of public attribute and method names.
    """
    attributes = dir(obj)
    return sorted([attr for attr in attributes if not attr.startswith("__")])


def return_patterns_and_guard_clauses() -> Dict[str, Any]:
    """Aggregates guard clause validation and dir() introspection demonstrations.

    Returns:
        Structured dictionary showcasing early return guard outputs and
        public method reflection on returned string and dictionary objects.
    """
    sample_none = validate_and_process_user(None)
    sample_empty = validate_and_process_user({})
    sample_underage = validate_and_process_user({"username": "Alice", "age": 16})
    sample_valid = validate_and_process_user({"username": "  Bob  ", "age": 25})

    str_public_methods = inspect_return_object("Python Return Tutorial")
    dict_public_methods = inspect_return_object({"key": "value"})

    return {
        "guard_results": {
            "none_input": sample_none,
            "empty_input": sample_empty,
            "underage_input": sample_underage,
            "valid_input": sample_valid,
        },
        "str_public_methods_count": len(str_public_methods),
        "str_sample_methods": str_public_methods[:5],
        "dict_public_methods": dict_public_methods,
    }


# =============================================================================
# 4. CROSS-VERSION EVOLUTION & BENCHMARK MATRIX
# =============================================================================

def return_vs_legacy_mechanics() -> Dict[str, Any]:
    """Provides a cross-version technical comparison of Python return mechanics.

    Returns:
        Dictionary outlining bytecode, AST, PEP milestones, and version features.
    """
    version_info = sys.version_info
    python_version_str = f"{version_info.major}.{version_info.minor}.{version_info.micro}"

    return {
        "interpreter_version": python_version_str,
        "bytecode_opcodes": {
            "RETURN_VALUE": "Pops top-of-stack (TOS) and returns control to caller frame",
            "RETURN_CONST": "Introduced in Python 3.12: Directly returns constant from co_consts without stack push",
        },
        "version_milestones": {
            "Python 2.7": "Generators forbid return values (SyntaxError); return types unannotated",
            "Python 3.3": "PEP 380: Generator return values supported via StopIteration(value) and yield from",
            "Python 3.5": "PEP 484: Type hints syntax introduced (def fn() -> ReturnType)",
            "Python 3.11": "typing.Never and typing.NoReturn standardized for non-returning functions",
            "Python 3.12": "RETURN_CONST opcode yields 5-10% performance gain for getter functions",
            "Python 3.13": "JIT adaptive instructions & zero-overhead frame evaluation for simple returns",
        },
        "python27_compatibility_notes": [
            "Use 'return' without argument inside generator functions in Python 2.7",
            "Use docstrings or Sphinx comments for return type documentation in Python 2.7",
        ],
    }


if __name__ == "__main__":
    print("=== Python Return Statement Tutorial Execution ===")
    import json
    print("\n--- Starter Examples ---")
    print(json.dumps(starter_return_examples(), indent=2))
    print("\n--- Advanced Mechanics ---")
    print(json.dumps(advanced_return_mechanics(), indent=2))
    print("\n--- Guard Clauses & Introspection ---")
    print(json.dumps(return_patterns_and_guard_clauses(), indent=2))
