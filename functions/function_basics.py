# Copyright (c) 2026 Teach Cloud / DilshadPython. All Rights Reserved.
# Unauthorized copying, re-hosting, scraping, or platform distribution is strictly prohibited.
# Official Platform: https://www.teach-cloud.net/ | Repository: https://github.com/dilshadpython

"""Python Function Architecture, Parameter Passing, LEGB Scope, Legacy 2.7 Comparison & Recursion Mechanics.

Import Notes & Architecture:
    - 'import sys': System parameter inspection, interpreter settings, and execution frame analysis.
    - 'import functools': Higher-order functions & functional tools (reduce, partial, wraps).
    - 'import inspect': Function signature inspection and dunder attribute introspection.
    - 'from typing import Dict, List, Any, Union, Tuple, Optional, Callable': PEP 484 static type hints.
"""

import sys
import functools
import inspect
from typing import Dict, List, Any, Union, Tuple, Optional, Callable

Number = Union[int, float]

# Global variable for scope demonstration
GLOBAL_COUNTER: int = 100


def starter_function_examples(
    name: str = "Developer",
    base_val: int = 10,
    *args: int,
    **kwargs: Any
) -> Dict[str, Any]:
    """Starter examples demonstrating parameter passing, default parameters, *args, **kwargs, and tuple returns.

    Inspired by DilshadPython/Python/Function scripts:
    - default_parameters.py
    - user_greeting.py
    - formatted_greeting.py
    - def_args_kwargs.py
    - args_unpacking.py
    - calculate_func.py
    - tuple_arithmetic.py
    """
    if not isinstance(name, str):
        raise TypeError("Input 'name' must be a valid string")
    if not isinstance(base_val, (int, float)):
        raise TypeError("Input 'base_val' must be a valid number")

    # 1. Default parameters and formatted greeting
    greeting_msg = f"Welcome, {name}! System Base Value: {base_val}"

    # 2. Dynamic positional argument unpacking (*args)
    args_sum = base_val + sum(args)

    # 3. Dynamic keyword argument unpacking (**kwargs)
    user_profile = {"name": name, "base_val": base_val}
    for key, value in kwargs.items():
        user_profile[key] = value

    # 4. Multiple return values via Tuple packing/unpacking
    def compute_stats(x: int, y: int) -> Tuple[int, int, float]:
        add_res = x + y
        mul_res = x * y
        avg_res = (x + y) / 2.0
        return add_res, mul_res, avg_res

    add_res, mul_res, avg_res = compute_stats(base_val, 5)

    return {
        "greeting_msg": greeting_msg,
        "args_sum": args_sum,
        "unpacked_args_count": len(args),
        "user_profile": user_profile,
        "arithmetic_stats": {
            "sum": add_res,
            "product": mul_res,
            "average": avg_res,
        },
    }


def scope_and_legb_rule(initial_value: int) -> Dict[str, Any]:
    """Demonstrates LEGB (Local, Enclosing, Global, Built-in) variable scope resolution and closure state.

    Inspired by DilshadPython/Python/Function scripts:
    - def_and_global_var.py
    - global_keyword.py
    - global_variable.py
    - nested_function_scope.py
    - nonlocal_scope_modify.py
    - closure_function.py
    """
    if not isinstance(initial_value, int):
        raise TypeError("Input 'initial_value' must be a valid integer")

    # 1. Global keyword modification
    global GLOBAL_COUNTER
    original_global = GLOBAL_COUNTER
    GLOBAL_COUNTER += initial_value
    modified_global = GLOBAL_COUNTER

    # 2. Local variable shadowing
    local_val = initial_value * 2

    # 3. Enclosing scope and Nonlocal keyword modification (Nested Functions & Closure)
    enclosing_counter = 50

    def inner_accumulator(increment: int) -> int:
        nonlocal enclosing_counter
        enclosing_counter += increment
        return enclosing_counter

    accumulated_1 = inner_accumulator(10)
    accumulated_2 = inner_accumulator(20)

    # 4. State-retaining Closure Factory
    def make_multiplier(factor: int) -> Callable[[int], int]:
        def multiplier(number: int) -> int:
            return number * factor
        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)

    return {
        "original_global": original_global,
        "modified_global": modified_global,
        "local_shadow_val": local_val,
        "enclosing_first_step": accumulated_1,
        "enclosing_second_step": accumulated_2,
        "closure_double_val": double(local_val),
        "closure_triple_val": triple(local_val),
    }


def functional_utilities_and_dispatch(
    items: List[int], op_name: str = "square"
) -> Dict[str, Any]:
    """Demonstrates lambdas, filter(), reduce(), higher-order functions, and dictionary dispatch tables.

    Inspired by DilshadPython/Python/Function scripts:
    - anonymous_func.py
    - higher_order_func.py
    - filter_func.py
    - reduce_func.py
    - dispatch_dict.py
    - dispatch_if.py
    - function_references.py
    """
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a valid Python list")

    # 1. Lambda functions & Anonymous execution
    square_lambda: Callable[[int], int] = lambda x: x ** 2
    squared_list: List[int] = [square_lambda(x) for x in items]

    # 2. Built-in filter() sequence processing
    even_items: List[int] = list(filter(lambda x: x % 2 == 0, items))

    # 3. Standard library functools.reduce() sequence accumulation
    product_reduction: int = functools.reduce(lambda x, y: x * y, items, 1)

    # 4. Dictionary Dispatch Table (emulating switch/case via function object references)
    dispatch_table: Dict[str, Callable[[List[int]], int]] = {
        "sum": sum,
        "max": max,
        "min": min,
        "product": lambda lst: functools.reduce(lambda a, b: a * b, lst, 1),
    }

    if op_name in dispatch_table:
        dispatch_result = dispatch_table[op_name](items)
    else:
        dispatch_result = sum(items)

    # 5. Higher-Order Function (accepts function as parameter)
    def apply_transform(data: List[int], func: Callable[[int], int]) -> List[int]:
        return [func(x) for x in data]

    cube_transform = apply_transform(items, lambda x: x ** 3)

    return {
        "squared_list": squared_list,
        "even_items": even_items,
        "product_reduction": product_reduction,
        "dispatch_operation": op_name,
        "dispatch_result": dispatch_result,
        "cube_transform": cube_transform,
    }


def recursion_mechanics(n: int, text: str) -> Dict[str, Any]:
    """Demonstrates recursive factorial computation, recursive sequence processing, and base/recursive cases.

    Inspired by DilshadPython/Python/Function scripts:
    - recursive_factorial.py
    - recursive_count_letter.py
    - recursive_duplicate.py
    - recursive_explode.py
    - recursive_string.py
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer")
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a valid string")

    # 1. Recursive Factorial
    def recursive_factorial(val: int) -> int:
        if val <= 1:
            return 1
        return val * recursive_factorial(val - 1)

    # 2. Recursive Character Counting
    def recursive_count_char(s: str, target: str) -> int:
        if not s:
            return 0
        match = 1 if s[0] == target else 0
        return match + recursive_count_char(s[1:], target)

    # 3. Recursive Consecutive Duplicate Deduplication
    def recursive_deduplicate(s: str) -> str:
        if len(s) <= 1:
            return s
        if s[0] == s[1]:
            return recursive_deduplicate(s[1:])
        return s[0] + recursive_deduplicate(s[1:])

    factorial_val = recursive_factorial(n)
    vowel_count = recursive_count_char(text.lower(), "a")
    dedup_text = recursive_deduplicate(text)

    return {
        "input_number": n,
        "factorial_result": factorial_val,
        "target_letter_count": vowel_count,
        "deduplicated_text": dedup_text,
    }


def legacy_python2_comparison_demo(point: Tuple[int, int], factor: int) -> Dict[str, Any]:
    """Demonstrates Python 2.7 legacy patterns vs Python 3 modern PEP 8 equivalents.

    Illustrates:
    - Python 2.7 tuple signature unpacking workaround vs Python 3 explicit tuple indexing/unpacking
    - Python 2.7 mutable list state workaround vs Python 3 nonlocal scope modification
    - Python 2.7 apply() builtin replacement with *args expansion
    - Python 2.7 func_* dunder attributes vs Python 3 __*__ attributes
    """
    if not isinstance(point, tuple) or len(point) != 2:
        raise TypeError("Input 'point' must be a 2-element tuple")

    # Python 3 explicit tuple unpacking (replacing legacy Py2 'def func((x, y)):')
    x, y = point
    scaled_point = (x * factor, y * factor)

    # Python 3 nonlocal state mutation (replacing legacy Py2 list wrapper 'state = [0]')
    counter = 0

    def increment_counter() -> int:
        nonlocal counter
        counter += 1
        return counter

    increment_counter()
    final_count = increment_counter()

    # Python 3 dynamic call (replacing legacy Py2 'apply(func, args)')
    def sample_func(a: int, b: int) -> int:
        return a + b

    dynamic_res = sample_func(*point)

    return {
        "scaled_point": scaled_point,
        "closure_state_counter": final_count,
        "dynamic_unpacking_result": dynamic_res,
        "dunder_name": sample_func.__name__,
        "dunder_code": str(sample_func.__code__),
    }


def execute_all_dir_function_methods() -> Dict[str, Any]:
    """Demonstrates built-in dunder attributes and inspection methods available on Python function objects."""
    def target_function(a: int, b: str = "default") -> Tuple[int, str]:
        """Sample function docstring for introspection."""
        return a, b

    func_dir = [attr for attr in dir(target_function) if not attr.startswith("__")]
    sig = inspect.signature(target_function)

    return {
        "function_name": target_function.__name__,
        "docstring": target_function.__doc__,
        "annotations": target_function.__annotations__,
        "defaults": target_function.__defaults__,
        "parameter_names": list(sig.parameters.keys()),
        "public_attributes": func_dir,
        "is_callable": callable(target_function),
    }


def cross_version_function_analysis() -> Dict[str, Any]:
    """Provides cross-version analysis for Python functions (Python 2.7 to 3.13 evolution)."""
    def positional_and_kwonly_demo(a: int, /, b: int, *, c: int = 30) -> int:
        """Python 3.8+ positional-only (/) and keyword-only (*) parameters syntax."""
        return a + b + c

    res = positional_and_kwonly_demo(10, 20, c=30)
    sig = inspect.signature(positional_and_kwonly_demo)

    return {
        "python_version": sys.version,
        "positional_and_kwonly_result": res,
        "has_positional_only_params": any(
            p.kind == inspect.Parameter.POSITIONAL_ONLY for p in sig.parameters.values()
        ),
        "has_keyword_only_params": any(
            p.kind == inspect.Parameter.KEYWORD_ONLY for p in sig.parameters.values()
        ),
    }
