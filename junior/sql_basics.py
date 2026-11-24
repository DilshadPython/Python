"""
SQL Basics Tutorial & In-Memory SQLite Studio Runner
Teach Cloud - Cloud, DevOps, and Python Backend Development

This module provides a beginner-friendly interactive interface for executing
relational SQL operations (CREATE, READ/SELECT, UPDATE, DELETE) using Python's
built-in sqlite3 engine, alongside foundational starter modules.
"""

import sqlite3
from typing import Dict, List, Any, Optional, Tuple

from cloud_app.tutorials.sqlite_db import (
    create_connection,
    close_connection,
    create_table,
    setup_database,
    dynamic_insert_data,
    run_beginner_tutorial,
    read_all_records,
    read_filtered_records,
    read_by_user_input,
    read_by_multiple_inputs,
    read_with_limit,
    update_records,
    delete_records,
    delete_records_with_commit,
    process_email_log,
)


class SQLStudioRunner:
    """
    In-memory SQLite database runner for interactive tutorial execution.
    Allows beginners to test DDL (Data Definition Language) and DML
    (Data Manipulation Language) safely.
    """

    def __init__(self, db_name: str = ":memory:"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._init_schema()

    def _init_schema(self) -> None:
        """Initialize a standard 'users' table schema for CRUD tutorials."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'developer',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def create_user(
        self, username: str, email: str, role: str = "developer"
    ) -> Dict[str, Any]:
        """
        [CREATE / INSERT]
        Inserts a new user record into the database.
        """
        if not username or not email:
            raise ValueError("Username and email are required fields.")

        query = "INSERT INTO users (username, email, role) VALUES (?, ?, ?)"
        self.cursor.execute(query, (username, email, role))
        self.conn.commit()
        user_id = self.cursor.lastrowid
        return {
            "status": "created",
            "id": user_id,
            "username": username,
            "email": email,
            "role": role,
        }

    def get_users(self, role: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        [READ / SELECT]
        Retrieves user records, optionally filtered by role.
        """
        if role:
            query = "SELECT id, username, email, role, created_at FROM users WHERE role = ? ORDER BY id ASC"
            self.cursor.execute(query, (role,))
        else:
            query = "SELECT id, username, email, role, created_at FROM users ORDER BY id ASC"
            self.cursor.execute(query)

        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def update_user_email(self, user_id: int, new_email: str) -> Dict[str, Any]:
        """
        [UPDATE]
        Updates the email address of an existing user by ID.
        """
        if not new_email:
            raise ValueError("New email cannot be empty.")

        # Check if user exists
        self.cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not self.cursor.fetchone():
            raise KeyError(f"User with ID {user_id} not found.")

        query = "UPDATE users SET email = ? WHERE id = ?"
        self.cursor.execute(query, (new_email, user_id))
        self.conn.commit()
        return {"status": "updated", "id": user_id, "new_email": new_email}

    def delete_user(self, user_id: int) -> Dict[str, Any]:
        """
        [DELETE]
        Removes a user record by ID.
        """
        self.cursor.execute("SELECT username FROM users WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        if not row:
            raise KeyError(f"User with ID {user_id} not found.")

        username = row["username"]
        query = "DELETE FROM users WHERE id = ?"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()
        return {"status": "deleted", "id": user_id, "deleted_username": username}

    def execute_raw_sql(
        self, sql_query: str, params: Tuple[Any, ...] = ()
    ) -> Tuple[List[Dict[str, Any]], str]:
        """
        Executes a raw SQL statement safely and returns rows + status message.
        """
        sql_trim = sql_query.strip()
        self.cursor.execute(sql_trim, params)
        if sql_trim.upper().startswith("SELECT"):
            rows = [dict(r) for r in self.cursor.fetchall()]
            return rows, f"SELECT returned {len(rows)} row(s)."
        else:
            self.conn.commit()
            return (
                [],
                f"Query executed successfully. Affected rows: {self.cursor.rowcount}",
            )

    def close(self) -> None:
        """Close SQLite database connection."""
        self.conn.close()


def run_sql_demo() -> Dict[str, Any]:
    """
    Demonstrates full CRUD operations lifecycle in SQLite.
    Returns structured results for tutorial verification.
    """
    db = SQLStudioRunner()

    # 1. CREATE
    u1 = db.create_user("monika_dev", "monika@teachcloud.dev", "backend_lead")
    u2 = db.create_user("alex_cloud", "alex@teachcloud.dev", "devops_engineer")

    # 2. READ
    all_users = db.get_users()

    # 3. UPDATE
    upd = db.update_user_email(u1["id"], "monika_lead@teachcloud.dev")

    # 4. DELETE
    del_res = db.delete_user(u2["id"])

    remaining = db.get_users()
    db.close()

    return {
        "created_users": [u1, u2],
        "initial_select": all_users,
        "update_result": upd,
        "delete_result": del_res,
        "final_select": remaining,
    }


if __name__ == "__main__":
    res = run_sql_demo()
    print("--- SQL CRUD DEMO COMPLETE ---")
    print("Final Active Users:", res["final_select"])
