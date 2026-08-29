"""
Backwards-compatible wrapper alias for number_square.py (descriptive filename).
"""
from Function.number_square import square

__all__ = ["square"]

if __name__ == '__main__':
    print(f"5 squared is: {square(5)}")
