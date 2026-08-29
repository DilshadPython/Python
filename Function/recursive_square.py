"""
Backwards-compatible wrapper alias for function_references.py (descriptive filename).
"""
from Function.function_references import square

__all__ = ["square"]

if __name__ == '__main__':
    print(square(5))
