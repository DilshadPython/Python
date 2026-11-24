"""
PostgreSQL Database Creation Module (`create_db.py`).

This module provides utility functions for connecting to the administrative PostgreSQL engine
and executing database creation DDL commands in `autocommit` mode.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import os`: Environment variable configuration interface.
# - `import sys`: System utilities for CLI exit status.
# - `import psycopg2`: PostgreSQL database interface adapter.
# - `from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT`: Isolation level constant.
# =========================================================================
import os
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(
    new_db_name: str = "university",
    user: str | None = None,
    password: str | None = None,
    host: str | None = None,
    port: str | None = None,
) -> bool:
    """Create a new PostgreSQL database.

    Args:
        new_db_name (str): Target database name to create.
        user (str | None): Admin DB user.
        password (str | None): Admin DB password.
        host (str | None): Database host address.
        port (str | None): Database port number.

    Returns:
        bool: True if created successfully, False otherwise.
    """
    admin_user = user or os.getenv("DB_USER", "dilmac")
    admin_password = password or os.getenv("DB_PASSWORD", "secret_pass")
    admin_host = host or os.getenv("DB_HOST", "127.0.0.1")
    admin_port = port or os.getenv("DB_PORT", "5432")

    connection = None
    try:
        # Connect to default 'postgres' administrative database
        connection = psycopg2.connect(
            database="postgres",
            user=admin_user,
            password=admin_password,
            host=admin_host,
            port=admin_port,
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with connection.cursor() as cursor:
            # Create database DDL command
            cursor.execute(f"CREATE DATABASE {new_db_name};")
            print(f"Database '{new_db_name}' created successfully.")
            return True

    except (Exception, psycopg2.Error) as error:
        print(f"Failed to create database '{new_db_name}': {error}")
        return False
    finally:
        if connection:
            connection.close()


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for database creation."""
    target_db = argv[1] if argv and len(argv) > 1 else "university"
    success = create_database(new_db_name=target_db)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
