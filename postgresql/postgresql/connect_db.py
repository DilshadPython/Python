"""
Backward-compatible wrapper script for database connection and record insertion.

This module delegates to `insert_mobile_record.py` for structured database insertion.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for process exit code handling.
# - `from insert_mobile_record import insert_mobile_record`: Insertion worker helper.
# =========================================================================
import sys

try:
    from postgresql.postgresql.insert_mobile_record import insert_mobile_record
except ImportError:
    from insert_mobile_record import insert_mobile_record


def run_legacy_demo() -> None:
    """Run legacy database insertion demonstration."""
    insert_mobile_record(mobile_id=5, model="One Plus 6", price=950.00)


if __name__ == "__main__":
    run_legacy_demo()
