"""
Backwards-compatible wrapper alias for closure_function.py (corrected spelling).
"""
from Function.closure_function import make_multiplier

__all__ = ["make_multiplier"]

if __name__ == "__main__":
    double = make_multiplier(2)
    print(f"Double 5: {double(5)}")
