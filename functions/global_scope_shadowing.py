"""
Demonstrates nested variable scope without nonlocal keyword (variable shadowing).
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple

x: str = 'Global x'


def outer_scope_shadowing() -> Tuple[str, str]:
    """Demonstrate local variable shadowing inside nested function scope."""
    x_outer = 'out side x'
    x_inner = ''
    def inner_scope_shadowing() -> str:
        nonlocal x_inner
        x_inner = 'in side x'
        return x_inner
    inner_scope_shadowing()
    return x_inner, x_outer


if __name__ == '__main__':
    inner_val, outer_val = outer_scope_shadowing()
    print(f"Inner: {inner_val} | Outer: {outer_val} | Global: {x}")
