"""
Unit Test Suite for SQLite Modules.

Tests all SQLite operations including table creation, insertion, reading,
updating, deleting, and log counting in isolated temporary database environments.
"""

import os
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from sqlite_db.connect_db import connect_database
from sqlite_db.create_table import create_car_table
from sqlite_db.insert_static_data import setup_database
from sqlite_db.read_all_data import read_all_records
from sqlite_db.read_filtered_data import read_filtered_records
from sqlite_db.read_by_user_input import read_by_user_input
from sqlite_db.read_by_multiple_inputs import read_by_multiple_inputs
from sqlite_db.read_with_limit import read_with_limit
from sqlite_db.update_data import update_records
from sqlite_db.delete_data import delete_records
from sqlite_db.delete_data_with_commit import delete_records_with_commit
from sqlite_db.email_counter_crud import process_email_log
from sqlite_db.beginner_starter import run_beginner_tutorial


class TestSQLiteModules(unittest.TestCase):
    """Test suite covering SQLite database module operations."""

    def setUp(self) -> None:
        """Create a temporary database file for each test case."""
        self.temp_db_fd, self.temp_db_path = tempfile.mkstemp(suffix=".db")
        os.close(self.temp_db_fd)

    def tearDown(self) -> None:
        """Clean up temporary files after test completion."""
        if os.path.exists(self.temp_db_path):
            os.remove(self.temp_db_path)

    def test_connect_database(self) -> None:
        """Test database connection initialization and closure."""
        conn = connect_database(self.temp_db_path)
        self.assertIsNotNone(conn)

    def test_create_car_table(self) -> None:
        """Test Car table creation."""
        create_car_table(self.temp_db_path)
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Car'")
            table = cursor.fetchone()
            self.assertIsNotNone(table)
            self.assertEqual(table[0], "Car")

    def test_insert_static_data(self) -> None:
        """Test batch static insertion of records."""
        setup_database(self.temp_db_path)
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Car")
            count = cursor.fetchone()[0]
            self.assertEqual(count, 8)

    def test_read_all_records(self) -> None:
        """Test querying all records from Car table."""
        setup_database(self.temp_db_path)
        with patch("sys.stdout"):
            read_all_records(self.temp_db_path)

    def test_read_filtered_records(self) -> None:
        """Test querying records matching specific brand condition."""
        setup_database(self.temp_db_path)
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Car WHERE Name = 'Audi'")
            audi_count = cursor.fetchone()[0]
            self.assertEqual(audi_count, 4)

        with patch("sys.stdout"):
            read_filtered_records("Audi", self.temp_db_path)

    def test_read_by_user_input(self) -> None:
        """Test searching records with user prompt input."""
        setup_database(self.temp_db_path)
        with patch("builtins.input", return_value="BMW"), patch("sys.stdout"):
            read_by_user_input(self.temp_db_path)

    def test_read_by_multiple_inputs(self) -> None:
        """Test searching records with compound user inputs."""
        setup_database(self.temp_db_path)
        with patch("builtins.input", side_effect=["Audi", "2017"]), patch("sys.stdout"):
            read_by_multiple_inputs(self.temp_db_path)

    def test_read_with_limit(self) -> None:
        """Test query pagination using LIMIT."""
        setup_database(self.temp_db_path)
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Car LIMIT 3")
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 3)

        with patch("sys.stdout"):
            read_with_limit(2, self.temp_db_path)

    def test_update_records(self) -> None:
        """Test updating matching database records."""
        setup_database(self.temp_db_path)
        update_records("Audi", "Audi-Updated", self.temp_db_path)
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Car WHERE Name = 'Audi-Updated'")
            updated_count = cursor.fetchone()[0]
            self.assertEqual(updated_count, 4)

    def test_delete_records(self) -> None:
        """Test record deletion operations."""
        setup_database(self.temp_db_path)
        with patch("sys.stdout"):
            delete_records("BMW", self.temp_db_path)

        delete_records_with_commit("Audi", self.temp_db_path)
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Car WHERE Name = 'Audi'")
            remaining_audi = cursor.fetchone()[0]
            self.assertEqual(remaining_audi, 0)

    def test_email_counter_crud(self) -> None:
        """Test log parsing and email aggregation CRUD operations."""
        temp_log_fd, temp_log_path = tempfile.mkstemp(suffix=".txt")
        os.close(temp_log_fd)
        try:
            with open(temp_log_path, "w", encoding="utf-8") as f:
                f.write("From: test1@example.com Sat Jan 5 2008\n")
                f.write("From: test2@example.com Sat Jan 5 2008\n")
                f.write("From: test1@example.com Sat Jan 5 2008\n")

            process_email_log(temp_log_path, self.temp_db_path)

            with sqlite3.connect(self.temp_db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT count FROM Counts WHERE email = 'test1@example.com'")
                row = cursor.fetchone()
                self.assertIsNotNone(row)
                self.assertEqual(row[0], 2)
        finally:
            if os.path.exists(temp_log_path):
                os.remove(temp_log_path)

    def test_beginner_starter_tutorial(self) -> None:
        """Test full execution of beginner starter tutorial."""
        with patch("sys.stdout"):
            run_beginner_tutorial(self.temp_db_path)


if __name__ == "__main__":
    unittest.main()
