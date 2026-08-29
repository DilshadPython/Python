"""
Demonstrates nested function lexical scope and variable shadowing.
"""


def outer_func() -> str:
    """Outer function defining local variable 'Bird' shadowed by nested inner function."""
    x = 'Bird'
    def inner_func() -> str:
        x = 'Dog'
        return x
    return inner_func()


if __name__ == '__main__':
    print("Nested inner x value:", outer_func())
