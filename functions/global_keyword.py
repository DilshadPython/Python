"""
Demonstrates using the  keyword to modify module-level global state.
"""

a: int = 12


def test_global_modify() -> int:
    """Increment global variable  by 3 and return new value."""
    global a
    a += 3
    return a


if __name__ == '__main__':
    print("Modified global a:", test_global_modify())
