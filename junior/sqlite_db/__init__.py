"""
SQLite Database Tutorial Modules.

This package provides foundational modules for learning relational database operations
with Python's built-in sqlite3 standard library.
"""

from .connect_db import create_connection, close_connection
from .create_table import create_table
from .insert_static_data import setup_database
from .insert_dynamic_data import dynamic_insert_data
from .beginner_starter import run_beginner_tutorial
from .read_all_data import read_all_records
from .read_filtered_data import read_filtered_records
from .read_by_user_input import read_by_user_input
from .read_by_multiple_inputs import read_by_multiple_inputs
from .read_with_limit import read_with_limit
from .update_data import update_records
from .delete_data import delete_records
from .delete_data_with_commit import delete_records_with_commit
from .email_counter_crud import process_email_log

__all__ = [
    "create_connection",
    "close_connection",
    "create_table",
    "setup_database",
    "dynamic_insert_data",
    "run_beginner_tutorial",
    "read_all_records",
    "read_filtered_records",
    "read_by_user_input",
    "read_by_multiple_inputs",
    "read_with_limit",
    "update_records",
    "delete_records",
    "delete_records_with_commit",
    "process_email_log",
]
