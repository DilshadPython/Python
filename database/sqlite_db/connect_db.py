"""
SQLite Connection Demonstration Module.

This script demonstrates connecting to an SQLite database, initializing a cursor,
and safely closing the database connection.

Note: Do NOT name python files 'sqlite3.py' to prevent shadowing the standard library module.
"""

import sqlite3
from typing import Optional


def connect_database(db_name: str = "mydatabase.db") -> Optional[sqlite3.Connection]:
    """Connect to SQLite database file.

    Args:
        db_name (str): Database file path or name.

    Returns:
        Optional[sqlite3.Connection]: SQLite connection object if successful.
    """
    try:
        # Establish connection to the database
        connection = sqlite3.connect(db_name)
        # Initialize cursor for executing queries
        cursor = connection.cursor()
        print(f"Successfully connected to database '{db_name}'.")

        # Close database connection
        connection.close()
        print("Database connection closed successfully.")
        return connection
    except sqlite3.Error as error:
        print(f"Error connecting to database: {error}")
        return None


if __name__ == "__main__":
    connect_database()
