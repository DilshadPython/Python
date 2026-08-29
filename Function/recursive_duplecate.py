"""
Backwards-compatible wrapper alias for recursive_duplicate.py (corrected spelling).
"""
from Function.recursive_duplicate import remove_duplicate, remove_duplecate

__all__ = ["remove_duplicate", "remove_duplecate"]

if __name__ == "__main__":
    print(remove_duplicate("Pyythhoon"))
