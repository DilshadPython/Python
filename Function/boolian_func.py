"""
Backwards-compatible wrapper alias for boolean_func.py (corrected spelling).
"""
from Function.boolean_func import is_even, is_positive

__all__ = ["is_even", "is_positive"]

if __name__ == "__main__":
    print(f"Is 10 even? {is_even(10)}")
    print(f"Is -5 positive? {is_positive(-5)}")
