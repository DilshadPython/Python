"""
Unit Test Suite for MySQL Manager Module.

Tests configuration initialization, connection state validation, fallback behavior,
and mock database execution methods.
"""

import unittest
from unittest.mock import MagicMock, patch

from mysql_db import MySQLDatabaseManager, HAS_MYSQL_CONNECTOR


class TestMySQLDatabaseManager(unittest.TestCase):
    """Test suite for MySQLDatabaseManager class."""

    def setUp(self) -> None:
        """Set up test connection parameters."""
        self.config = {
            "host": "localhost",
            "user": "test_user",
            "password": "test_password",
            "database": "test_db",
            "port": 3306
        }
        self.manager = MySQLDatabaseManager(self.config)

    def test_init_config(self) -> None:
        """Test configuration assignment upon initialization."""
        self.assertEqual(self.manager.config, self.config)
        self.assertIsNone(self.manager.connection)

    def test_disconnect_when_no_connection(self) -> None:
        """Test disconnect behavior when no connection exists."""
        with patch("sys.stdout"):
            self.manager.disconnect()
        self.assertIsNone(self.manager.connection)

    def test_execute_query_without_connection(self) -> None:
        """Test execute_query returns empty list when connection is inactive."""
        results = self.manager.execute_query("SELECT * FROM Users")
        self.assertEqual(results, [])

    def test_execute_update_without_connection(self) -> None:
        """Test execute_update returns 0 affected rows when connection is inactive."""
        affected = self.manager.execute_update("UPDATE Users SET name='test'")
        self.assertEqual(affected, 0)

    @unittest.skipUnless(HAS_MYSQL_CONNECTOR, "Requires mysql-connector-python package")
    @patch("mysql.connector.connect")
    def test_connect_and_query_mock(self, mock_connect: MagicMock) -> None:
        """Test MySQL connection and query execution with mock objects."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.is_connected.return_value = True
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(1, "Alice"), (2, "Bob")]
        mock_connect.return_value = mock_conn

        # Test connect
        connected = self.manager.connect()
        self.assertTrue(connected)

        # Test execute_query with mock
        results = self.manager.execute_query("SELECT * FROM Users WHERE id = %s", (1,))
        self.assertEqual(results, [(1, "Alice"), (2, "Bob")])
        mock_cursor.execute.assert_called_with("SELECT * FROM Users WHERE id = %s", (1,))

        # Test execute_update with mock
        mock_cursor.rowcount = 1
        affected = self.manager.execute_update("UPDATE Users SET name=%s WHERE id=%s", ("Alice Updated", 1))
        self.assertEqual(affected, 1)

        # Test disconnect
        self.manager.disconnect()
        mock_conn.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
