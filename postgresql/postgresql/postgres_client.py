"""
PostgreSQL Client Database Connection & Query Wrapper (`PostgreSQLClient`).

This module provides a production-grade interface for managing PostgreSQL connections,
executing parameterized queries securely (`%s`), handling transactions, and falling back
to environment variables for sensitive database credentials.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import os`: System environment module for retrieving DB credentials.
# - `import psycopg2`: PEP 249 compliant PostgreSQL database adapter.
# - `from psycopg2.extensions import connection as PgConnection`: Connection type hint.
# - `from typing import Any, Dict, List, Optional, Tuple`: PEP 484 type hint generics.
# =========================================================================
import os
from typing import Any, List, Optional, Tuple
import psycopg2


class PostgreSQLClient:
    """Production-grade PostgreSQL database adapter wrapper."""

    def __init__(
        self,
        db_name: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[str] = None,
    ) -> None:
        """Initialize PostgreSQL connection configuration with environment variable fallbacks.

        Args:
            db_name (Optional[str]): Database name (defaults to DB_NAME env or 'university').
            user (Optional[str]): Database username (defaults to DB_USER env or 'dilmac').
            password (Optional[str]): Database password (defaults to DB_PASSWORD env).
            host (Optional[str]): Host address (defaults to DB_HOST env or '127.0.0.1').
            port (Optional[str]): Port number (defaults to DB_PORT env or '5432').
        """
        self.db_name = db_name or os.getenv("DB_NAME", "university")
        self.user = user or os.getenv("DB_USER", "dilmac")
        self.password = password or os.getenv("DB_PASSWORD", "secret_pass")
        self.host = host or os.getenv("DB_HOST", "127.0.0.1")
        self.port = port or os.getenv("DB_PORT", "5432")

    def connect(self) -> Any:
        """Establish connection to PostgreSQL database.

        Returns:
            Any: psycopg2 connection object.
        """
        return psycopg2.connect(
            database=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> int:
        """Execute non-query DDL or DML statement (CREATE, INSERT, UPDATE, DELETE).

        Args:
            query (str): SQL query string containing `%s` placeholders.
            params (Optional[Tuple[Any, ...]]): Tuple of parameter values.

        Returns:
            int: Affected row count.
        """
        connection = self.connect()
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params or ())
                    rowcount = cursor.rowcount
            return rowcount
        finally:
            connection.close()

    def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
        """Execute SELECT query and return all matching record rows.

        Args:
            query (str): SQL SELECT query string.
            params (Optional[Tuple[Any, ...]]): Tuple of parameter values.

        Returns:
            List[Tuple[Any, ...]]: List of fetched tuple records.
        """
        connection = self.connect()
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params or ())
                    return cursor.fetchall()
        finally:
            connection.close()
