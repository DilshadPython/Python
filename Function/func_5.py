"""
Backwards-compatible wrapper alias for calculator_dict.py (descriptive filename).
"""
from Function.calculator_dict import calculator

__all__ = ["calculator"]

if __name__ == '__main__':
    print("Calculator results:", calculator(17, 36))
