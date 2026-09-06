"""
SQLite Dynamic User Input Query Demonstration Module.

This script prompts the user for a search parameter and executes a parameterized SQL SELECT query.
"""

import sqlite3


def read_by_user_input(db_name: str = "mydatabase.db") -> None:
    """Prompt user for a car brand and fetch matching database records.

    Args:
        db_name (str): SQLite database file name.
    """
    car_name = input("Please enter the Car name to search: ").strip()

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Car WHERE Name = ?"

        print(f"\n--- Search Results for '{car_name}' ---")
        cursor.execute(query, (car_name,))
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)
        else:
            print(f"No records found for car name '{car_name}'.")


if __name__ == "__main__":
    read_by_user_input()
