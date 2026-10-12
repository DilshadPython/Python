"""
Security and SQL Injection Prevention Test Suite.

Verifies that parameterized SQL queries defend against SQL Injection vulnerabilities
(such as tautology attacks, UNION attacks, and piggybacked statement execution).
"""

import os
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from sqlite_db.insert_static_data import setup_database
from sqlite_db.read_by_user_input import read_by_user_input
from sqlite_db.read_by_multiple_inputs import read_by_multiple_inputs


class TestSQLInjectionSecurity(unittest.TestCase):
    """Security unit test suite targeting SQL injection vectors."""

    def setUp(self) -> None:
        """Create a temporary database populated with static test data."""
        self.temp_db_fd, self.temp_db_path = tempfile.mkstemp(suffix=".db")
        os.close(self.temp_db_fd)
        setup_database(self.temp_db_path)

    def tearDown(self) -> None:
        """Remove temporary database file."""
        if os.path.exists(self.temp_db_path):
            os.remove(self.temp_db_path)

    def test_sql_injection_tautology_attack(self) -> None:
        """Test SQL Injection tautology payload: ' OR '1'='1 ."""
        malicious_input = "' OR '1'='1"

        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            # Execute safely using parameterized query
            cursor.execute("SELECT * FROM Car WHERE Name = ?", (malicious_input,))
            results = cursor.fetchall()
            # Should return 0 rows because literal name "' OR '1'='1" does not exist
            self.assertEqual(len(results), 0)

    def test_sql_injection_drop_table_attempt(self) -> None:
        """Test SQL Injection piggybacked DROP TABLE payload."""
        malicious_input = "Audi'; DROP TABLE Car; --"

        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Car WHERE Name = ?", (malicious_input,))
            results = cursor.fetchall()
            self.assertEqual(len(results), 0)

            # Verify that Car table was NOT dropped and still intact
            cursor.execute("SELECT COUNT(*) FROM Car")
            count = cursor.fetchone()[0]
            self.assertEqual(count, 8)

    def test_sql_injection_union_attack(self) -> None:
        """Test SQL Injection UNION query payload."""
        malicious_input = "' UNION SELECT 1, 2, 3, 4 --"

        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Car WHERE Name = ?", (malicious_input,))
            results = cursor.fetchall()
            self.assertEqual(len(results), 0)

    def test_read_by_user_input_security(self) -> None:
        """Test read_by_user_input function safely handles malicious search strings."""
        malicious_input = "BMW' OR 1=1--"
        with patch("builtins.input", return_value=malicious_input), patch("sys.stdout"):
            read_by_user_input(self.temp_db_path)

        # Verify database integrity remains untouched
        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Car")
            self.assertEqual(cursor.fetchone()[0], 8)

    def test_read_by_multiple_inputs_security(self) -> None:
        """Test read_by_multiple_inputs function safely handles malicious strings."""
        malicious_name = "' OR 'a'='a"
        malicious_version = "2017' OR '1'='1"
        with patch("builtins.input", side_effect=[malicious_name, malicious_version]), patch("sys.stdout"):
            read_by_multiple_inputs(self.temp_db_path)

        with sqlite3.connect(self.temp_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Car")
            self.assertEqual(cursor.fetchone()[0], 8)


if __name__ == "__main__":
    unittest.main()
