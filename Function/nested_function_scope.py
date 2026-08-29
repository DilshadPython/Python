"""
Demonstrates nested function calls and distinct variable scopes.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple


def outer_nested_scope() -> Tuple[str, str]:
    """Return values of local variables from inner and outer scopes."""
    x = 'This is local var in out_side() called x'
    inner_val = ''
    def inner_nested_scope() -> str:
        nonlocal inner_val
        inner_val = 'This is local var in in_side() called x'
        return inner_val
    inner_nested_scope()
    return inner_val, x


if __name__ == '__main__':
    res_in, res_out = outer_nested_scope()
    print("Inner:", res_in)
    print("Outer:", res_out)
