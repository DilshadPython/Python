"""
SQLite Persistent Delete with Transaction Commit Module.

This script demonstrates executing SQL DELETE statements and committing changes
to permanently delete records from disk storage.
"""

import sqlite3


def delete_records_with_commit(target_brand: str = "Audi", db_name: str = "mydatabase.db") -> None:
    """Delete matching records and commit transaction to database disk file.

    Args:
        target_brand (str): Car brand name to delete.
        db_name (str): SQLite database file name.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        delete_sql = "DELETE FROM Car WHERE Name = ?"
        cursor.execute(delete_sql, (target_brand,))

        # Explicit transaction commit
        connection.commit()
        print(f"Committed delete operation for brand '{target_brand}'. Deleted {cursor.rowcount} rows.")

        print("\n--- Remaining Records in Database ---")
        cursor.execute("SELECT * FROM Car")
        for row in cursor.fetchall():
            print(row)


if __name__ == "__main__":
    delete_records_with_commit()
