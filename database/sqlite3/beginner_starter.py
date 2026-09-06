"""
Beginner's Guide to Python & SQLite Databases.

This script is designed for absolute beginners learning database concepts.
It covers core definitions, database connections, table creation, data types,
and the fundamental CRUD operations (Create, Read, Update, Delete).

--- Core Database Terminology ---
- Database: An organized collection of structured data stored electronically.
- Table: A grid of rows and columns (like a spreadsheet tab) holding related data.
- Column / Field: A specific attribute of data (e.g., 'id', 'name', 'price').
- Row / Record: A single entry containing data for all columns.
- Primary Key: A unique identifier for each row in a table.
- SQL (Structured Query Language): The language used to communicate with databases.

--- SQLite Standard Data Types ---
- NULL: Represents missing or unknown values.
- INTEGER: Whole numbers (e.g., 1, 42, 2026).
- REAL: Floating-point numbers (e.g., 19.99, 3.14).
- TEXT: String of characters (e.g., 'Alice', 'Laptop').
- BLOB: Binary data (e.g., images, files, raw bytes).
"""

import sqlite3


def run_beginner_tutorial(db_name: str = "starter_demo.db") -> None:
    """Demonstrate end-to-end database operations for beginners."""

    print("=== Step 1: Connecting to the Database ===")
    # sqlite3.connect() opens a file database. If the file doesn't exist, it creates it!
    with sqlite3.connect(db_name) as connection:
        # A cursor is like a control mechanism to execute SQL commands and fetch results.
        cursor = connection.cursor()

        print("\n=== Step 2: Creating a Table (CREATE TABLE) ===")
        # CREATE TABLE defines the structure (schema) and column data types.
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER DEFAULT 0
            )
            """
        )
        print("Table 'Products' created successfully!")

        print("\n=== Step 3: Inserting Data (CREATE / INSERT) ===")
        # Insert initial data into the Products table
        sample_products = [
            ("Wireless Mouse", 25.50, 100),
            ("Mechanical Keyboard", 89.99, 45),
            ("HD Monitor 27-inch", 199.99, 20),
            ("USB-C Hub", 15.00, 150)
        ]

        # executemany inserts multiple rows safely using parameterized placeholders (?)
        cursor.executemany(
            "INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)",
            sample_products
        )
        # Save (commit) changes to the database file on disk
        connection.commit()
        print(f"Inserted {len(sample_products)} products.")

        print("\n=== Step 4: Reading Data (READ / SELECT) ===")
        # SELECT * retrieves all columns from the specified table
        cursor.execute("SELECT id, name, price, quantity FROM Products")
        all_rows = cursor.fetchall()

        for row in all_rows:
            product_id, name, price, qty = row
            print(f"ID: {product_id} | Name: {name:<20} | Price: ${price:<6.2f} | Stock: {qty}")

        print("\n=== Step 5: Filtering Data (WHERE Clause) ===")
        # WHERE filters rows based on a condition (e.g., price > 50)
        min_price = 50.0
        cursor.execute("SELECT name, price FROM Products WHERE price > ?", (min_price,))
        expensive_items = cursor.fetchall()

        print(f"Products costing more than ${min_price}:")
        for item in expensive_items:
            print(f"- {item[0]}: ${item[1]:.2f}")

        print("\n=== Step 6: Updating Data (UPDATE) ===")
        # UPDATE modifies existing records matching a condition
        new_price = 19.99
        target_name = "Wireless Mouse"
        cursor.execute("UPDATE Products SET price = ? WHERE name = ?", (new_price, target_name))
        connection.commit()
        print(f"Updated '{target_name}' price to ${new_price}.")

        print("\n=== Step 7: Deleting Data (DELETE) ===")
        # DELETE removes rows matching a condition
        delete_target = "USB-C Hub"
        cursor.execute("DELETE FROM Products WHERE name = ?", (delete_target,))
        connection.commit()
        print(f"Deleted '{delete_target}' from inventory.")

        print("\n=== Step 8: Final Inventory State ===")
        cursor.execute("SELECT id, name, price, quantity FROM Products")
        for row in cursor.fetchall():
            print(row)

    print("\nDatabase operations completed cleanly.")


if __name__ == "__main__":
    run_beginner_tutorial()
