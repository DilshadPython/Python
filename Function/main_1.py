"""
Backwards-compatible wrapper alias for greeting_handler.py (descriptive filename).
"""
from Function.greeting_handler import hello, main

__all__ = ["hello", "main"]

if __name__ == '__main__':
    print(main("Dilshad"))
