"""
SQLite Static Insertion Demonstration Module.

This script demonstrates creating a table and populating it with static records
using SQL INSERT statements and committing changes to persist data.
"""

import sqlite3


def setup_database(db_name: str = "mydatabase.db") -> None:
    """Create Car table and insert static sample records.

    Args:
        db_name (str): SQLite database filename.
    """
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        # Create Car table if not existing
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

        # Insert static dataset
        cars_data = [
            ('Audi', 'A5', 2017, 'Brand new zero miles'),
            ('Audi', 'A3', 2015, 'Used 160 000 miles'),
            ('Audi', 'A7', 2016, 'New 35 000 miles'),
            ('Audi', 'A2', 2005, 'Used 61 233 miles'),
            ('BMW', 'XZ', 2010, 'Brand new zero miles'),
            ('Porsche', 'P10', 2014, 'New been used 10 000 miles'),
            ('Mercedes', 'ML', 2017, 'Brand new 1000 miles'),
            ('Ford', 'F16', 2018, 'New test only 15 000 miles')
        ]

        cursor.executemany(
            "INSERT INTO Car (Name, Model, Version, Description) VALUES (?, ?, ?, ?)",
            cars_data
        )

        # Commit changes to persist inserted rows into disk storage
        connection.commit()
        print(f"Successfully inserted {len(cars_data)} static records into Car table.")


if __name__ == "__main__":
    setup_database()
