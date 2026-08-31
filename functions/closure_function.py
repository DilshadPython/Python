"""
Demonstrates function closures retaining enclosing scope state.
"""
# Import explanation:
# 'from typing import Callable' imports Callable to type-annotate functions returned by outer functions.
from typing import Callable


def make_multiplier(factor: float) -> Callable[[float], float]:
    """Return a closure function that multiplies its argument by factor."""
    def multiply(number: float) -> float:
        return number * factor
    return multiply


if __name__ == "__main__":
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")
