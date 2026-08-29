"""
Backwards-compatible wrapper alias for recursive_factorial_v2.py (descriptive filename).
"""
from Function.recursive_factorial_v2 import factorial_recur

__all__ = ["factorial_recur"]

if __name__ == '__main__':
    print(factorial_recur(5))
