"""
Backward-compatible wrapper script for UUID generation.

This file delegates to `uuid_generator.py`, providing structured UUID v1 and v4
demonstration functions.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for execution status.
# - `from uuid_generator import generate_uuid_v1, generate_uuid_v4`:
#   Functions for generating timestamp-based and random UUIDs.
# =========================================================================
import sys

try:
    from unicode_strings.uuid_generator import generate_uuid_v1, generate_uuid_v4
except ImportError:
    from uuid_generator import generate_uuid_v1, generate_uuid_v4


def run_uuid_demo() -> None:
    """Demonstrate UUID v1 and UUID v4 generation."""
    print("--- UUID v1 Demonstration ---")
    for u1 in generate_uuid_v1(10):
        print(u1)

    print("\n--- UUID v4 Demonstration ---")
    for u4 in generate_uuid_v4(4):
        print(u4)


if __name__ == "__main__":
    run_uuid_demo()
