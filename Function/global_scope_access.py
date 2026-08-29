"""
Demonstrates reading outer/global scope variables from nested inner function scope.
"""

x: str = 'Global x'


def outer_global_access() -> str:
    """Access global variable inside nested function."""
    def inner_global_access() -> str:
        return x
    return inner_global_access()


if __name__ == '__main__':
    print("Nested access to global x:", outer_global_access())
