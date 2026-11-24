"""Return Advanced Demonstration Module.

This module demonstrates advanced return patterns in Python, including:
1. Returning callables/closures from higher-order functions.
2. Return statement precedence and behavior within try...finally blocks.
3. Return statements in generator functions (PEP 380 StopIteration value passing).
4. Modern return type annotations (Callable, NoReturn, Never).
"""

# import standard typing tools for modern return type hints
import sys
from typing import Callable, Generator, NoReturn, Union


def create_multiplier(factor: float) -> Callable[[float], float]:
    """Demonstrate returning a function (closure) from another function.

    Args:
        factor: The multiplication factor to encapsulate.

    Returns:
        A callable function that takes a float and returns a float.
    """
    def multiplier(number: float) -> float:
        return number * factor

    return multiplier


def execute_finally_return_demo(override: bool) -> str:
    """Demonstrate return statement interactions inside try...finally blocks.

    IMPORTANT: A return statement inside a `finally` block will override any
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
            # WARNING: Returning from finally overrides try return values
            return "Return overridden by finally block"


def generator_with_return_value(limit: int) -> Generator[int, None, str]:
    """Demonstrate return statement behavior inside a generator function (PEP 380).

    In Python 3.3+, generator functions can include a `return value` statement.
    The returned value is attached to the `StopIteration` exception when the
    generator finishes iteration or is consumed by `yield from`.

    Args:
        limit: Number of items to yield.

    Yields:
        Integers from 0 up to limit - 1.

    Returns:
        A summary status string upon completion.
    """
    for i in range(limit):
        yield i
    return f"Completed generator iteration up to {limit}"


def consume_generator(limit: int) -> tuple[list[int], str]:
    """Helper function to consume a generator and extract its return value.

    Args:
        limit: Generator count limit.

    Returns:
        A tuple containing (list of yielded items, generator return value string).
    """
    gen = generator_with_return_value(limit)
    items = []
    return_value = ""
    while True:
        try:
            items.append(next(gen))
        except StopIteration as e:
            # In Python 3.3+, e.value contains the return statement payload
            return_value = e.value
            break
    return items, return_value


def raise_fatal_error(message: str) -> NoReturn:
    """Demonstrate typing.NoReturn annotation for functions that never return.

    Functions that raise exceptions or terminate processes without returning
    control use NoReturn (or typing.Never in Python 3.11+).

    Args:
        message: Error message string.

    Raises:
        RuntimeError: Always raised to demonstrate NoReturn.
    """
    raise RuntimeError(f"Fatal error encountered: {message}")


if __name__ == "__main__":
    print("=== Python Return Advanced Demonstration ===")

    # 1. Higher-order function returning a closure
    double = create_multiplier(2.0)
    triple = create_multiplier(3.0)
    print(f"Double of 7: {double(7.0)}")
    print(f"Triple of 7: {triple(7.0)}")

    # 2. Try-finally return precedence
    normal_flow = execute_finally_return_demo(override=False)
    override_flow = execute_finally_return_demo(override=True)
    print(f"Normal try-finally flow: '{normal_flow}'")
    print(f"Overridden try-finally flow: '{override_flow}'")

    # 3. Generator with return value (PEP 380)
    yielded_vals, final_status = consume_generator(4)
    print(f"Yielded values: {yielded_vals}")
    print(f"Generator return value (StopIteration.value): '{final_status}'")

    # 4. NoReturn demonstration
    print("Testing NoReturn function exception catch:")
    try:
        raise_fatal_error("System resource unavailable")
    except RuntimeError as err:
        print(f"Caught expected NoReturn exception: {err}")
