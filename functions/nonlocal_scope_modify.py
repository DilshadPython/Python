"""
Demonstrates modifying outer scope variables using the  keyword.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple


def outer_nonlocal_modify() -> Tuple[str, str]:
    """Modify outer scope local variable  from inside nested function."""
    x = 'This is local var in out_side() called x'
    initial_x = x
    def inner_nonlocal_modify() -> None:
        nonlocal x
        x = 'This is local var in in_side() called x'
    inner_nonlocal_modify()
    return initial_x, x


if __name__ == '__main__':
    before, after = outer_nonlocal_modify()
    print(f"Before nonlocal edit: {before}")
    print(f"After nonlocal edit: {after}")
