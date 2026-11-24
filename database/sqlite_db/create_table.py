"""
SQLite Table Creation Demonstration Module.

This script demonstrates connecting to an SQLite database and creating
a relational table schema using SQL DDL (Data Definition Language) statements.

Note: Do NOT name python scripts 'sqlite3.py' to avoid shadowing the standard library module.
"""

import sqlite3


def create_car_table(db_name: str = "mydatabase.db") -> None:
    """Connect to SQLite database and create the 'Car' table if it does not exist.

    Args:
        db_name (str): SQLite database file name.
    """
    # Establish connection to database file using context manager
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        # Create Car table with structured schema
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
        connection.commit()
        print("Table 'Car' successfully created or verified.")


if __name__ == "__main__":
    create_car_table()
