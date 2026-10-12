"""
SQLite Delete Operation Demonstration Module.

This script demonstrates executing SQL DELETE statements to remove records from a table.
"""

import sqlite3


def delete_records(target_brand: str = "Audi", db_name: str = "mydatabase.db") -> None:
    """Delete records matching criteria and display remaining dataset.

    Args:
        target_brand (str): Car brand to delete from table.
        db_name (str): SQLite database file name.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        print("--- Table Contents Before Delete ---")
        for row in cursor.execute("SELECT * FROM Car"):
            print(row)

        print(f"\nDeleting records where Name = '{target_brand}'...")
        cursor.execute("DELETE FROM Car WHERE Name = ?", (target_brand,))

        print("\n--- Table Contents After Delete (In Active Transaction) ---")
        cursor.execute("SELECT * FROM Car")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    delete_records()
