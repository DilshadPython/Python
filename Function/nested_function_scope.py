"""
Demonstrates nested function calls and distinct variable scopes.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple


def out_side() -> Tuple[str, str]:
    """Return values of local variables from inner and outer scopes."""
    x = 'This is local var in out_side() called x'
    inner_val = ''
    def in_side() -> str:
        nonlocal inner_val
        inner_val = 'This is local var in in_side() called x'
        return inner_val
    in_side()
    return inner_val, x


if __name__ == '__main__':
    res_in, res_out = out_side()
    print("Inner:", res_in)
    print("Outer:", res_out)
