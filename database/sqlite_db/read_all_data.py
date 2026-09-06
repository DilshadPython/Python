"""
SQLite Read All Records Demonstration Module.

This script demonstrates querying and displaying all rows stored in an SQLite table.
"""

import sqlite3


def read_all_records(db_name: str = "mydatabase.db") -> None:
    """Fetch and print all rows from Car table.

    Args:
        db_name (str): SQLite database file name.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Car"

        print("--- Fetching All Records ---")
        for row in cursor.execute(query):
            print(f"Full Row: {row} | Car Name: {row[0]}")


if __name__ == "__main__":
    read_all_records()
