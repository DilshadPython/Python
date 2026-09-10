"""
PostgreSQL Mobile Record Insertion Module (`insert_mobile_record.py`).

This module demonstrates creating a `mobile` table and inserting record tuples using
parameterized SQL queries (`%s`) to protect against SQL injection vulnerabilities.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Tuple, Any`: PEP 484 type hint generics.
# - `from postgres_client import PostgreSQLClient`: Client database adapter helper.
# =========================================================================
import sys
from typing import Any, Tuple

try:
    from postgresql.postgresql.postgres_client import PostgreSQLClient
except ImportError:
    from postgres_client import PostgreSQLClient


def ensure_mobile_table(client: PostgreSQLClient) -> None:
    """Ensure the `mobile` table exists before inserting records."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS mobile (
        ID INT PRIMARY KEY,
        MODEL VARCHAR(100) NOT NULL,
        PRICE NUMERIC(10, 2) NOT NULL
    );
    """
    client.execute_query(create_table_sql)


def insert_mobile_record(
    mobile_id: int,
    model: str,
    price: float,
    client: PostgreSQLClient | None = None,
) -> bool:
    """Insert a single mobile device record into the database.

    Args:
        mobile_id (int): Unique device ID.
        model (str): Smartphone model name.
        price (float): Price amount.
        client (PostgreSQLClient | None): Database client instance.

    Returns:
        bool: True if inserted successfully, False otherwise.
    """
    db_client = client or PostgreSQLClient()

    try:
        ensure_mobile_table(db_client)

        insert_sql = "INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s, %s, %s)"
        record_params: Tuple[Any, ...] = (mobile_id, model, price)

        rowcount = db_client.execute_query(insert_sql, record_params)
        print(f"{rowcount} Record inserted successfully into mobile table: ({mobile_id}, {model}, {price})")
        return True
    except Exception as error:
        print(f"Failed to insert record into mobile table: {error}")
        return False


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for mobile record insertion."""
    success = insert_mobile_record(mobile_id=5, model="One Plus 6", price=950.00)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
