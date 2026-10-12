"""
SQLite Query Pagination / LIMIT Demonstration Module.

This script demonstrates limiting query result counts using the SQL LIMIT clause.
"""

import sqlite3


def read_with_limit(limit_count: int = 2, db_name: str = "mydatabase.db") -> None:
    """Fetch maximum specified number of rows from Car table.

    Args:
        limit_count (int): Maximum number of rows to retrieve.
        db_name (str): SQLite database file name.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Car LIMIT ?"

        print(f"--- Fetching First {limit_count} Records ---")
        cursor.execute(query, (limit_count,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)


if __name__ == "__main__":
    read_with_limit()
