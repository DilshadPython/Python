"""
Beginner Level PostgreSQL Demonstration Module.

This module provides clear, well-commented examples of basic PostgreSQL database operations
designed for beginner developers (`connect`, `execute`, `fetchall`, `commit`, `close`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import os`: Environment variable configuration interface.
# - `import sys`: System utilities for CLI execution.
# - `import psycopg2`: Standard CPython PostgreSQL database adapter.
# - `from typing import Any, List, Tuple`: PEP 484 type hint generics.
# =========================================================================
import os
import sys
from typing import Any, List, Tuple
import psycopg2


def beginner_connect_db() -> Any:
    """Establish a simple connection to PostgreSQL database.

    Returns:
        Any: psycopg2 connection object.
    """
    user = os.getenv("DB_USER", "dilmac")
    password = os.getenv("DB_PASSWORD", "secret_pass")
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "5432")
    database = os.getenv("DB_NAME", "university")

    return psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
    )


def simple_insert_student(name: str, gender: str, about: str) -> bool:
    """Insert a student record using basic step-by-step psycopg2 execution.

    Args:
        name (str): Student full name.
        gender (str): Gender string.
        about (str): Short bio description.

    Returns:
        bool: True if inserted successfully, False otherwise.
    """
    connection = None
    try:
        connection = beginner_connect_db()
        cursor = connection.cursor()

        # SQL INSERT query using %s placeholders
        insert_sql = "INSERT INTO Students (Name, Gender, About) VALUES (%s, %s, %s);"
        cursor.execute(insert_sql, (name, gender, about))

        # Commit transaction to persist changes
        connection.commit()
        print(f"Beginner: Student '{name}' inserted successfully.")
        cursor.close()
        return True

    except Exception as error:
        print(f"Beginner Insert Error: {error}")
        return False
    finally:
        if connection:
            connection.close()


def simple_select_students() -> List[Tuple[Any, ...]]:
    """Retrieve all student records using basic SELECT fetchall().

    Returns:
        List[Tuple[Any, ...]]: List of fetched student tuple rows.
    """
    connection = None
    records: List[Tuple[Any, ...]] = []
    try:
        connection = beginner_connect_db()
        cursor = connection.cursor()

        cursor.execute("SELECT Name, Gender, About FROM Students;")
        records = cursor.fetchall()
        cursor.close()

    except Exception as error:
        print(f"Beginner Select Error: {error}")
    finally:
        if connection:
            connection.close()

    return records


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner PostgreSQL demonstration."""
    print("=== Beginner Level PostgreSQL Demonstration ===")
    simple_insert_student("Alice Smith", "Female", "Computer Science Major")
    students = simple_select_students()
    print("Fetched Students:", students)
    return 0


if __name__ == "__main__":
    sys.exit(main())
