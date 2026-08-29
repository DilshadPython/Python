"""
Backwards-compatible wrapper alias for greeting_welcome.py (descriptive filename).
"""
from Function.greeting_welcome import welcome

__all__ = ["welcome"]

if __name__ == '__main__':
    print(welcome("Hello", "Dilshad"))
