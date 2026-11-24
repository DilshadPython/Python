"""
PostgreSQL Table Creation Module (`create_table.py`).

This module provides functions for executing SQL DDL statements to create database tables
(e.g., `Students` table with Name, Gender, and About fields).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI argument processing.
# - `from postgres_client import PostgreSQLClient`: Client wrapper helper.
# =========================================================================
import sys

try:
    from postgresql.postgresql.postgres_client import PostgreSQLClient
except ImportError:
    from postgres_client import PostgreSQLClient


def create_students_table(client: PostgreSQLClient | None = None) -> bool:
    """Create the `Students` table in the target PostgreSQL database.

    Args:
        client (PostgreSQLClient | None): Database client instance.

    Returns:
        bool: True if table created successfully, False otherwise.
    """
    db_client = client or PostgreSQLClient()
    create_sql = """
    CREATE TABLE IF NOT EXISTS Students (
        ID SERIAL PRIMARY KEY,
        Name VARCHAR(120) NOT NULL,
        Gender VARCHAR(10),
        About TEXT
    );
    """

    try:
        db_client.execute_query(create_sql)
        print("Table 'Students' created successfully.")
        return True
    except Exception as error:
        print(f"Failed to create 'Students' table: {error}")
        return False


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for table creation."""
    success = create_students_table()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
