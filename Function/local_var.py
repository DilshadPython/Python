"""
Backwards-compatible wrapper alias for nonlocal_scope_read.py (descriptive filename).
"""
from Function.nonlocal_scope_read import out_side

__all__ = ["out_side"]

if __name__ == '__main__':
    print(out_side())
