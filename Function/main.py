"""
Backwards-compatible wrapper alias for script_main_entry.py (descriptive filename).
"""
from Function.script_main_entry import hello, main

__all__ = ["hello", "main"]

if __name__ == '__main__':
    print(main("World"))
