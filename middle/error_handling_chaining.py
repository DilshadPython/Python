"""
Track 04: Advanced Exception Architecture

Description: Master Mid-Level Exception Architecture: Custom exception hierarchies, Exception Chaining (raise ... from ...), Exception Groups (except*), and production error patterns.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/error_handling_chaining
"""

# --- Code Snippet 1 ---
class ApplicationError(Exception):
    """Base exception for all application errors."""
    pass

class DatabaseConnectionError(ApplicationError):
    """Raised when database host fails to respond."""
    pass

class DataValidationError(ApplicationError):
    """Raised when inbound JSON payload violates domain constraints."""
    pass

try:
    raise DataValidationError("Field 'email' is required.")
except ApplicationError as err:
    print(f"Caught Application Level Error: {type(err).__name__} -> {err}")

# --- Code Snippet 2 ---
import json

def parse_user_config(raw_json: str) -> dict:
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as err:
        # Explicitly chain JSONDecodeError into DataValidationError
        raise DataValidationError("Failed to parse configuration JSON payload") from err

try:
    parse_user_config("invalid_json_str{")
except DataValidationError as exc:
    print("Handled Exception:", exc)
    print("Underlying Root Cause:", repr(exc.__cause__))

# --- Code Snippet 3 ---
# Python 3.11+ Exception Group Example
eg = ExceptionGroup(
    "Batch Task Failures",
    [
        ValueError("Invalid User ID"),
        TypeError("Expected string, got int"),
        KeyError("Missing 'auth_token' key")
    ]
)

try:
    raise eg
except* ValueError as eg_val:
    print("Handled ValueErrors:", eg_val.exceptions)
except* (TypeError, KeyError) as eg_type:
    print("Handled Type & Key Errors:", eg_type.exceptions)

