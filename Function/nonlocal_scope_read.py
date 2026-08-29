"""
Demonstrates scope inspection using  modifier inside nested functions.
"""


def out_side() -> str:
    """Access outer function scope variable via nonlocal."""
    x = 'This is local var in out_side() called x'
    res = ''
    def in_side() -> None:
        nonlocal res
        res = x
    in_side()
    return res


if __name__ == '__main__':
    print("Nonlocal read:", out_side())
