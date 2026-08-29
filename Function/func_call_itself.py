"""
Backwards-compatible wrapper alias for nested_scope_shadowing.py (descriptive filename).
"""
from Function.nested_scope_shadowing import outer_func

__all__ = ["outer_func"]

if __name__ == '__main__':
    print("Nested inner x value:", outer_func())
