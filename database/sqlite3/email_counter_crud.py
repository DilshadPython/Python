"""
SQLite Email Aggregation & CRUD Demonstration Module.

This script parses mail log header lines (e.g. from 'mailbox-short.txt'), extracts sender email addresses,
and maintains an aggregated count of emails per sender in an SQLite table.

Reference: https://www.sqlite.org/lang_select.html
"""

import os
import sqlite3
from typing import Optional


def process_email_log(file_path: str = "mailbox-short.txt", db_name: str = "New_db.sqlite") -> None:
    """Read mail log file and aggregate email counts in SQLite database.

    Args:
        file_path (str): Log text file path.
        db_name (str): SQLite database file name.
    """
    if not os.path.exists(file_path):
        print(f"Log file '{file_path}' not found. Creating a sample '{file_path}' for demonstration...")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008\n")
            f.write("From: louis@media.berkeley.edu Fri Jan  4 18:10:48 2008\n")
            f.write("From: zqian@umich.edu Fri Jan  4 16:10:39 2008\n")
            f.write("From: rjlowe@iupui.edu Fri Jan  4 15:46:24 2008\n")
            f.write("From: zqian@umich.edu Fri Jan  4 15:03:18 2008\n")

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        # Reset table for fresh calculation
        cursor.execute("DROP TABLE IF EXISTS Counts")
        cursor.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

        with open(file_path, "r", encoding="utf-8") as fh:
            for line in fh:
                if not line.startswith("From: "):
                    continue
                pieces = line.split()
                if len(pieces) < 2:
                    continue
                email = pieces[1]

                # Check if email entry already exists in database
                cursor.execute("SELECT count FROM Counts WHERE email = ?", (email,))
                row: Optional[tuple] = cursor.fetchone()

                if row is None:
                    # Insert initial count of 1 (Note: tuple syntax (email,) is required)
                    cursor.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email,))
                else:
                    # Increment count for existing email entry
                    cursor.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email,))

        connection.commit()

        # Retrieve top 10 email senders by count descending
        sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"
        print("\n--- Top 10 Email Senders ---")
        for row in cursor.execute(sqlstr):
            print(f"Email: {row[0]:<30} | Count: {row[1]}")


if __name__ == "__main__":
    file_input = input("Enter log file name (default 'mailbox-short.txt'): ").strip()
    if not file_input:
        file_input = "mailbox-short.txt"
    process_email_log(file_input)
