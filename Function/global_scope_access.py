"""
Demonstrates reading outer/global scope variables from nested inner function scope.
"""

x: str = 'Global x'


def out_side() -> str:
    """Access global variable inside nested function."""
    def in_side() -> str:
        return x
    return in_side()


if __name__ == '__main__':
    print("Nested access to global x:", out_side())
