"""
Demonstrates local variable declaration inside nested inner functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple

x: str = 'Global x'


def out_side() -> Tuple[str, str]:
    """Execute inner function with local scope variable."""
    x_local = 'out side x'
    inner_res = ''
    def in_side() -> str:
        nonlocal inner_res
        inner_res = 'in side x'
        return inner_res
    in_side()
    return inner_res, x_local


if __name__ == '__main__':
    print(out_side())
