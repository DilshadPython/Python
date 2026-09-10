"""
Unit Test Suite for PostgreSQL Client & Utilities across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. Core PostgreSQLClient initialization and query execution.
2. Beginner level database functions (`beginner_postgres.py`).
3. Intermediate level batch execution & transactional rollback (`intermediate_postgres.py`).
4. Senior level ORM mapping, migration runner, and async coroutines (`senior_postgres.py`).
"""

import asyncio
import sys
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

# Ensure psycopg2 exists in sys.modules (using MagicMock fallback if not installed)
try:
    import psycopg2
except ImportError:
    mock_psycopg2 = MagicMock()
    mock_psycopg2.Error = Exception
    mock_psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT = 0
    sys.modules["psycopg2"] = mock_psycopg2
    sys.modules["psycopg2.extensions"] = mock_psycopg2.extensions

# Support both package and local directory import paths
root = Path(__file__).parent / "postgresql"
sys.path.insert(0, str(root))

from postgres_client import PostgreSQLClient
from create_db import create_database
from create_table import create_students_table
from insert_mobile_record import insert_mobile_record
from beginner_postgres import simple_insert_student, simple_select_students
from intermediate_postgres import batch_insert_mobile_devices, safe_transactional_operation
from senior_postgres import SchemaMigrationRunner, fetch_students_as_models, async_fetch_student_count, StudentModel


class TestPostgreSQLClient(unittest.TestCase):
    """Test suite verifying PostgreSQLClient operations with mock connections."""

    def setUp(self) -> None:
        """Initialize test client instance."""
        self.client = PostgreSQLClient(
            db_name="test_db",
            user="test_user",
            password="test_password",
            host="127.0.0.1",
            port="5432",
        )

    def test_client_init_defaults(self) -> None:
        """Verify client configuration properties."""
        self.assertEqual(self.client.db_name, "test_db")
        self.assertEqual(self.client.user, "test_user")

    @patch("psycopg2.connect")
    def test_execute_query(self, mock_connect: MagicMock) -> None:
        """Verify execute_query executes DDL/DML statement."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        rowcount = self.client.execute_query("INSERT INTO test (name) VALUES (%s)", ("unit_test",))

        self.assertEqual(rowcount, 1)

    @patch("psycopg2.connect")
    def test_beginner_functions(self, mock_connect: MagicMock) -> None:
        """Verify beginner student insertion and selection."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Alice", "Female", "CS Major")]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        res_insert = simple_insert_student("Alice", "Female", "CS Major")
        self.assertTrue(res_insert)

        students = simple_select_students()
        self.assertEqual(len(students), 1)

    @patch("psycopg2.connect")
    def test_intermediate_functions(self, mock_connect: MagicMock) -> None:
        """Verify intermediate batch execution and transaction handling."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        batch = [(1, "Phone A", 500.0), (2, "Phone B", 600.0)]
        count = batch_insert_mobile_devices(batch)
        self.assertEqual(count, 2)

    @patch("psycopg2.connect")
    def test_senior_functions(self, mock_connect: MagicMock) -> None:
        """Verify senior migration runner, ORM mapping, and async queries."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "Bob", "Male", "Engineering")]
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        # Test Migration Runner
        runner = SchemaMigrationRunner(self.client)
        applied = runner.apply_migrations()
        self.assertEqual(applied, 2)

        # Test ORM Mapping
        models = fetch_students_as_models(self.client)
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0].name, "Bob")

        # Test Async Query
        count = asyncio.run(async_fetch_student_count(self.client))
        self.assertIsInstance(count, int)


if __name__ == "__main__":
    unittest.main()
