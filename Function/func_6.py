"""
Backwards-compatible wrapper alias for tuple_arithmetic.py (descriptive filename).
"""
from Function.tuple_arithmetic import add_and_subtract_three

__all__ = ["add_and_subtract_three"]

if __name__ == '__main__':
    print(add_and_subtract_three(6, 8, 9))
