"""
Demonstrates positional vs keyword default parameters in Python function definitions.
"""


def myfunc(a: int, b: int = 1) -> int:
    """Add required parameter  and optional default keyword parameter ."""
    return a + b


if __name__ == '__main__':
    print("myfunc(4) ->", myfunc(4))
    print("myfunc(8, 7) ->", myfunc(8, 7))
