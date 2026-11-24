"""
Demonstrates local variable declaration inside nested inner functions.
"""
from typing import Tuple

x: str = 'Global x'


def inner_local_scope() -> Tuple[str, str]:
    """Execute inner function with local scope variable."""
    x_local = 'out side x'
    inner_res = ''
    def inner_local_func() -> str:
        nonlocal inner_res
        inner_res = 'in side x'
        return inner_res
    inner_local_func()
    return inner_res, x_local


if __name__ == '__main__':
    print(inner_local_scope())
