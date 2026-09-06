"""
MySQL Database Manager Module.

This script demonstrates connecting to a MySQL database server and executing
DDL/DML SQL statements using `mysql-connector-python` or `pymysql`.

Note: MySQL is an external database service. Unlike SQLite (which is built-in
and file-based), MySQL requires an active server and library installation.

Install dependencies via:
    pip install -r requirements.txt
"""

from typing import Any, Dict, List, Optional, Tuple

try:
    import mysql.connector
    from mysql.connector import Error as MySQLError
    HAS_MYSQL_CONNECTOR = True
except ImportError:
    HAS_MYSQL_CONNECTOR = False


class MySQLDatabaseManager:
    """Manager class for MySQL database connection and CRUD operations."""

    def __init__(self, config: Dict[str, Any]) -> None:
        """Initialize database manager with connection configuration.

        Args:
            config (Dict[str, Any]): Dictionary containing connection params:
                host, user, password, database, port.
        """
        self.config: Dict[str, Any] = config
        self.connection: Optional[Any] = None

    def connect(self) -> bool:
        """Establish connection to MySQL server.

        Returns:
            bool: True if connection succeeded, False otherwise.
        """
        if not HAS_MYSQL_CONNECTOR:
            print("Error: 'mysql-connector-python' is not installed.")
            print("Please install it using: pip install mysql-connector-python")
            return False

        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection and self.connection.is_connected():
                print("Successfully connected to MySQL database.")
                return True
        except MySQLError as err:
            print(f"Error connecting to MySQL: {err}")

        return False

    def disconnect(self) -> None:
        """Close current MySQL database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL database connection closed.")

    def create_table(self, query: str) -> None:
        """Execute a DDL table creation query.

        Args:
            query (str): SQL CREATE TABLE statement.
        """
        if not self.connection or not self.connection.is_connected():
            print("No active connection available.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Table created successfully.")
            cursor.close()
        except MySQLError as err:
            print(f"Failed to create table: {err}")

    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
        """Execute a SELECT query and return fetched records.

        Args:
            query (str): SQL SELECT query string.
            params (Optional[Tuple[Any, ...]]): Query parameters.

        Returns:
            List[Tuple[Any, ...]]: List of fetched table rows.
        """
        if not self.connection or not self.connection.is_connected():
            print("No active connection available.")
            return []

        results: List[Tuple[Any, ...]] = []
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
        except MySQLError as err:
            print(f"Failed to execute query: {err}")

        return results

    def execute_update(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> int:
        """Execute INSERT, UPDATE, or DELETE query and commit changes.

        Args:
            query (str): SQL DML statement.
            params (Optional[Tuple[Any, ...]]): Parameters for the query.

        Returns:
            int: Number of affected rows.
        """
        if not self.connection or not self.connection.is_connected():
            print("No active connection available.")
            return 0

        affected_rows: int = 0
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"Query executed successfully. Affected rows: {affected_rows}")
        except MySQLError as err:
            print(f"Failed to execute update: {err}")
            if self.connection:
                self.connection.rollback()

        return affected_rows


if __name__ == "__main__":
    # Example usage configuration (Update parameters for your MySQL server)
    db_config: Dict[str, Any] = {
        "host": "localhost",
        "user": "root",
        "password": "your_password",
        "database": "test_db",
        "port": 3306
    }

    db_manager = MySQLDatabaseManager(db_config)
    print("MySQLDatabaseManager module ready for integration.")
