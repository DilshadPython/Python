"""
Backwards-compatible wrapper alias for global_variable.py (corrected spelling).
"""
from Function.global_variable import increment_global_counter, get_counter_state

__all__ = ["increment_global_counter", "get_counter_state"]

if __name__ == "__main__":
    init_val, new_val = get_counter_state()
    print(f"Counter initial: {init_val}, updated: {new_val}")
