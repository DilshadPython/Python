"""
Demonstrates module-level global variable access and global keyword modification.
"""
# Import explanation:
# 'from typing import Tuple' imports Tuple from typing for function return type hints.
from typing import Tuple

# Module global variable
COUNTER: int = 100


def increment_global_counter(amount: int = 1) -> int:
    """Modify module-level global variable using global keyword."""
    global COUNTER
    COUNTER += amount
    return COUNTER


def get_counter_state() -> Tuple[int, int]:
    """Return initial and incremented counter values."""
    initial = COUNTER
    updated = increment_global_counter(10)
    return initial, updated


if __name__ == "__main__":
    init_val, new_val = get_counter_state()
    print(f"Counter initial: {init_val}, updated: {new_val}")
