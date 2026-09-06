"""
SQLite Record Update Demonstration Module.

This script demonstrates modifying existing database rows using the SQL UPDATE statement
and displaying updated table contents.
"""

import sqlite3


def update_records(old_name: str = "Audi", new_name: str = "a-Audi", db_name: str = "mydatabase.db") -> None:
    """Update row values matching target criteria.

    Args:
        old_name (str): Original car brand name to replace.
        new_name (str): Replacement car brand name.
        db_name (str): SQLite database file name.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        update_sql = "UPDATE Car SET Name = ? WHERE Name = ?"
        cursor.execute(update_sql, (new_name, old_name))
        connection.commit()
        print(f"Updated records where Name was '{old_name}' to '{new_name}'. Affected rows: {cursor.rowcount}")

        select_sql = "SELECT * FROM Car"
        print("\n--- Current Table Contents After Update ---")
        for row in cursor.execute(select_sql):
            print(row)


if __name__ == "__main__":
    update_records()
