"""
Demonstrates scope inspection using  modifier inside nested functions.
"""


def outer_nonlocal_read() -> str:
    """Access outer function scope variable via nonlocal."""
    x = 'This is local var in out_side() called x'
    res = ''
    def inner_nonlocal_read() -> None:
        nonlocal res
        res = x
    inner_nonlocal_read()
    return res


if __name__ == '__main__':
    print("Nonlocal read:", outer_nonlocal_read())
