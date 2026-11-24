"""
Intermediate Level PostgreSQL Demonstration Module.

This module provides functional database patterns designed for intermediate developers
(`with connection:` context managers, `executemany` batch execution, explicit `rollback()`, constraint recovery).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import os`: Environment variable configuration interface.
# - `import sys`: System utilities for CLI execution exit status.
# - `import psycopg2`: Standard PostgreSQL database adapter.
# - `from typing import Any, List, Tuple`: PEP 484 type hint generics.
# =========================================================================
import os
import sys
from typing import Any, List, Tuple
import psycopg2

try:
    from postgresql.postgresql.postgres_client import PostgreSQLClient
except ImportError:
    from postgres_client import PostgreSQLClient


def batch_insert_mobile_devices(records: List[Tuple[int, str, float]]) -> int:
    """Perform bulk record insertion using `cursor.executemany()` and context managers.

    Args:
        records (List[Tuple[int, str, float]]): List of (id, model, price) tuples.

    Returns:
        int: Number of batch records inserted.
    """
    client = PostgreSQLClient()
    connection = client.connect()

    batch_sql = "INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s, %s, %s);"

    try:
        # Context manager manages automatic commit on success and rollback on failure
        with connection:
            with connection.cursor() as cursor:
                cursor.executemany(batch_sql, records)
                rowcount = len(records)
                print(f"Intermediate: Batch inserted {rowcount} mobile records.")
                return rowcount
    except Exception as error:
        print(f"Intermediate Batch Insert Error: {error}")
        return 0
    finally:
        connection.close()


def safe_transactional_operation(record_a: Tuple[int, str, float], record_b: Tuple[int, str, float]) -> bool:
    """Demonstrate atomic multi-statement transaction with explicit `rollback()`.

    Args:
        record_a (Tuple[int, str, float]): First record tuple.
        record_b (Tuple[int, str, float]): Second record tuple.

    Returns:
        bool: True if transaction committed successfully, False if rolled back.
    """
    client = PostgreSQLClient()
    connection = client.connect()
    insert_sql = "INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s, %s, %s);"

    try:
        cursor = connection.cursor()

        # Step 1: Execute first statement
        cursor.execute(insert_sql, record_a)

        # Step 2: Execute second statement
        cursor.execute(insert_sql, record_b)

        # Commit all statements atomically
        connection.commit()
        cursor.close()
        print("Intermediate Transaction: Both records committed atomically.")
        return True

    except Exception as error:
        # Rollback transaction on any error (e.g. Duplicate Key Constraint)
        connection.rollback()
        print(f"Intermediate Transaction Rolled Back due to error: {error}")
        return False
    finally:
        connection.close()


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate PostgreSQL demonstration."""
    print("=== Intermediate Level PostgreSQL Demonstration ===")
    batch = [(10, "iPhone 15 Pro", 1199.99), (11, "Pixel 8 Pro", 999.99)]
    batch_insert_mobile_devices(batch)

    # Transaction with intentional primary key collision
    dup_a = (20, "Galaxy S24", 899.99)
    dup_b = (20, "Galaxy S24 Duplicate", 899.99)
    safe_transactional_operation(dup_a, dup_b)

    return 0


if __name__ == "__main__":
    sys.exit(main())
