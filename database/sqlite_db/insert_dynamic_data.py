"""
SQLite Dynamic Insertion Demonstration Module.

This script demonstrates accepting dynamic user inputs at runtime and safely inserting
them into an SQLite table using parameterized queries to protect against SQL injection.
"""

import sqlite3


def dynamic_insert_data(db_name: str = "mydatabase.db") -> None:
    """Prompt user for record details and insert them into database.

    Args:
        db_name (str): SQLite database file name.
    """
    dynamic_name = input("Enter Car name: ")
    dynamic_model = input("Enter Car model: ")
    dynamic_version = float(input("Enter year/version: "))
    dynamic_desc = input("Enter description: ")

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        # Ensure table exists
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Car (
                Name TEXT,
                Model TEXT,
                Version REAL,
                Description TEXT
            )
            """
        )

        # Parameterized insert query prevents SQL injection attacks
        cursor.execute(
            "INSERT INTO Car (Name, Model, Version, Description) VALUES (?, ?, ?, ?)",
            (dynamic_name, dynamic_model, dynamic_version, dynamic_desc)
        )
        connection.commit()
        print(f"Record for '{dynamic_name} {dynamic_model}' successfully inserted.")


if __name__ == "__main__":
    dynamic_insert_data()
