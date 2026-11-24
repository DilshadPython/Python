"""
Senior Level PostgreSQL Demonstration Module.

This module provides enterprise architecture patterns designed for senior software engineers
(dataclass ORM object mapping, connection pooling, asynchronous coroutine queries, and automated migration runner).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import asyncio`: Asynchronous I/O event loop for non-blocking database workflows.
# - `import os`: Environment variable management.
# - `import sys`: System execution utilities.
# - `from dataclasses import dataclass`: Lightweight ORM object data containers.
# - `from typing import Any, Dict, List, Optional`: PEP 484 type hint generics.
# =========================================================================
import asyncio
from dataclasses import dataclass
import os
import sys
from typing import Any, Dict, List, Optional

try:
    from postgresql.postgresql.postgres_client import PostgreSQLClient
except ImportError:
    from postgres_client import PostgreSQLClient


@dataclass
class StudentModel:
    """Dataclass mapping database rows to strongly-typed domain objects."""

    id: Optional[int]
    name: str
    gender: str
    about: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert student object to dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "about": self.about,
        }


class SchemaMigrationRunner:
    """Automated Database Schema Migration Utility."""

    MIGRATIONS: List[str] = [
        "CREATE TABLE IF NOT EXISTS schema_version (version INT PRIMARY KEY, applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);",
        "CREATE TABLE IF NOT EXISTS AuditLogs (ID SERIAL PRIMARY KEY, Action VARCHAR(255), CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP);",
    ]

    def __init__(self, client: PostgreSQLClient) -> None:
        """Initialize migration runner with database client instance."""
        self.client = client

    def apply_migrations(self) -> int:
        """Apply pending SQL schema migration DDL statements.

        Returns:
            int: Number of applied migrations.
        """
        applied_count = 0
        for sql in self.MIGRATIONS:
            try:
                self.client.execute_query(sql)
                applied_count += 1
            except Exception as error:
                print(f"Senior Migration Warning: {error}")
        print(f"Senior: Applied {applied_count} schema migrations successfully.")
        return applied_count


async def async_fetch_student_count(client: PostgreSQLClient) -> int:
    """Simulate asynchronous database metric query using `asyncio`.

    Args:
        client (PostgreSQLClient): Target database client.

    Returns:
        int: Total student count in database.
    """
    # Non-blocking async sleep simulating event-driven database fetch
    await asyncio.sleep(0.01)
    try:
        rows = client.fetch_all("SELECT COUNT(*) FROM Students;")
        return int(rows[0][0]) if rows else 0
    except Exception:
        return 0


def fetch_students_as_models(client: PostgreSQLClient) -> List[StudentModel]:
    """Execute query and map raw PostgreSQL tuples to `StudentModel` ORM objects.

    Args:
        client (PostgreSQLClient): Target database client.

    Returns:
        List[StudentModel]: List of strongly-typed domain objects.
    """
    query = "SELECT ID, Name, Gender, About FROM Students;"
    models: List[StudentModel] = []
    try:
        rows = client.fetch_all(query)
        for row in rows:
            models.append(StudentModel(id=row[0], name=row[1], gender=row[2], about=row[3]))
    except Exception as error:
        print(f"Senior ORM Mapping Error: {error}")

    return models


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior PostgreSQL demonstration."""
    print("=== Senior Level PostgreSQL Demonstration ===")
    client = PostgreSQLClient()

    # Apply database migrations
    migrator = SchemaMigrationRunner(client)
    migrator.apply_migrations()

    # Dataclass ORM Mapping
    students = fetch_students_as_models(client)
    print("Mapped Student Models:", [s.to_dict() for s in students])

    # Asynchronous query execution
    count = asyncio.run(async_fetch_student_count(client))
    print(f"Async Fetched Student Count: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
