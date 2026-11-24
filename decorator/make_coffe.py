"""Beverage preparation timing decorator (Coffee).

Demonstrates a parameterized beverage preparation decorator with clean type
hints and accurate spelling.
"""

import functools
import time
from typing import Any, Callable


def make_coffee(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator timing the coffee brewing process."""
    @functools.wraps(func)
    def mix_coffee(type_coffee: str, time_needed: float = 0.05) -> Any:
        start_time = time.perf_counter()
        result = func(type_coffee, time_needed)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Coffee ({type_coffee}) brew time: {elapsed:.4f} seconds.")
        return result

    return mix_coffee


# Backward compatibility aliases
make_coffe = make_coffee


@make_coffee
def new_coffee(type_coffee: str, time_needed: float = 0.05) -> str:
    """Brew a new cup of coffee."""
    time.sleep(time_needed)
    return f"{type_coffee} brewed successfully."


new_coffe = new_coffee


if __name__ == "__main__":
    result = new_coffee("Black Coffee", 0.1)
    print(result)
