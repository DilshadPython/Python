"""
Backwards-compatible wrapper alias for absolute_values.py (descriptive filename).
"""
from Function.absolute_values import calculate_abs_values

__all__ = ["calculate_abs_values"]

if __name__ == '__main__':
    print(calculate_abs_values(-2.45, -33, 12.68, 2 + 3j))
