"""
SQLite Conditional Read Demonstration Module.

This script demonstrates filtering query results using standard SQL WHERE conditions.
"""

import sqlite3


def read_filtered_records(car_brand: str = "Audi", db_name: str = "mydatabase.db") -> None:
    """Fetch and print records matching specific criteria.

    Args:
        car_brand (str): Brand name to filter by.
        db_name (str): SQLite database file name.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        # Standard SQL condition syntax using WHERE Name = ?
        query = "SELECT * FROM Car WHERE Name = ?"

        print(f"--- Fetching Records for Brand '{car_brand}' ---")
        cursor.execute(query, (car_brand,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)


if __name__ == "__main__":
    read_filtered_records()
