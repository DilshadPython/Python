"""
Backwards-compatible wrapper alias for global_inner_local.py (descriptive filename).
"""
from Function.global_inner_local import out_side

__all__ = ["out_side"]

if __name__ == '__main__':
    print(out_side())
