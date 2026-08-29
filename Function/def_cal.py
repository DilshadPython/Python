"""
Backwards-compatible wrapper alias for basic_calculator.py (descriptive filename).
"""
from Function.basic_calculator import calculator

__all__ = ["calculator"]

if __name__ == '__main__':
    print(calculator(20, 5))
