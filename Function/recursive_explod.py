"""
Backwards-compatible wrapper alias for recursive_explode.py (corrected spelling).
"""
from Function.recursive_explode import recursive_explode

__all__ = ["recursive_explode"]

if __name__ == "__main__":
    print(recursive_explode("Python"))
