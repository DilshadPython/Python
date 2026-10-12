"""
SQLite Multiple Parameter Query Demonstration Module.

This script prompts the user for multiple filter criteria (e.g. name and version/year)
and executes a compound SQL SELECT query.
"""

import sqlite3


def read_by_multiple_inputs(db_name: str = "mydatabase.db") -> None:
    """Prompt user for car brand and version year to perform compound SQL filtering.

    Args:
        db_name (str): SQLite database file name.
    """
    car_name = input("Enter car name: ").strip()
    car_version = input("Enter car version/year: ").strip()

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Car WHERE Name = ? AND Version = ?"

        print(f"\n--- Search Results for Name='{car_name}' and Version='{car_version}' ---")
        cursor.execute(query, (car_name, car_version))
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)
        else:
            print("No matching records found.")


if __name__ == "__main__":
    read_by_multiple_inputs()
