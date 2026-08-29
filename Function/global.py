"""
Backwards-compatible wrapper alias for global_keyword.py (descriptive filename).
"""
from Function.global_keyword import test_global_modify

__all__ = ["test_global_modify"]

if __name__ == '__main__':
    print("Modified global a:", test_global_modify())
