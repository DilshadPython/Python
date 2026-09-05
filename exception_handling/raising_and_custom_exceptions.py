"""
Python Exception Handling: Raising & Custom Exceptions (`raise ... from ...`)

This module demonstrates raising standard exceptions, defining custom exception
hierarchies inheriting from `Exception`, and utilizing Python 3 exception chaining.

Key Concepts:
- `raise ExceptionType(message)`: Explicitly triggers an exception.
- Custom Exceptions: Subclasses of `Exception` created to represent domain errors.
- Exception Chaining (`raise NewExc from cause`): Preserves original causal exception.
"""
from typing import Dict, Any


class ApplicationError(Exception):
    """Base custom exception for the application domain."""

    def __init__(self, message: str, code: int = 500) -> None:
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"


class ValidationError(ApplicationError):
    """Subclass representing input validation failures."""

    def __init__(self, field: str, message: str) -> None:
        super().__init__(f"Validation failed for field '{field}': {message}", code=400)
        self.field = field


class DatabaseConnectionError(ApplicationError):
    """Subclass representing database connectivity failures."""

    def __init__(self, db_name: str, cause: Exception) -> None:
        super().__init__(f"Database '{db_name}' connection error.", code=503)
        self.db_name = db_name
        self.__cause__ = cause


def register_user(user_data: Dict[str, Any]) -> str:
    """
    Validates user data and raises custom ValidationError on failure.

    Args:
        user_data (Dict[str, Any]): Registration payload.

    Returns:
        str: Success confirmation message.

    Raises:
        ValidationError: If username or age fails domain validation.
    """
    if "username" not in user_data or not user_data["username"]:
        raise ValidationError("username", "Username is required and cannot be empty.")

    age = user_data.get("age", 0)
    if not isinstance(age, int) or age < 18:
        raise ValidationError("age", f"Age must be an integer >= 18. Got: {age!r}")

    return f"User '{user_data['username']}' successfully registered."


def connect_database(db_url: str) -> None:
    """
    Simulates database connection failure with explicit exception chaining (`raise ... from ...`).

    Args:
        db_url (str): Database connection URL.

    Raises:
        DatabaseConnectionError: Wraps underlying OSError/TimeoutError.
    """
    try:
        # Simulate underlying system socket error
        raise TimeoutError("Socket connection timed out after 5000ms.")
    except TimeoutError as original_error:
        # Explicit exception chaining using `raise ... from original_error`
        raise DatabaseConnectionError("production_db", original_error) from original_error


def main() -> None:
    """Demonstrates custom exceptions and exception chaining."""
    print("=" * 60)
    print("5. Raising Custom Exceptions & Exception Chaining (`raise ... from ...`)")
    print("=" * 60)

    # 1. Custom ValidationError handling
    print("\n--- Custom ValidationError Demonstration ---")
    invalid_user = {"username": "john_doe", "age": 15}
    try:
        register_user(invalid_user)
    except ValidationError as val_err:
        print(f"Trapped ValidationError: {val_err}")
        print(f"  Field: {val_err.field!r}, Code: {val_err.code}")

    # 2. Exception Chaining Demonstration
    print("\n--- Exception Chaining (`raise ... from ...`) Demonstration ---")
    try:
        connect_database("db://localhost:5432")
    except DatabaseConnectionError as db_err:
        print(f"Trapped High-Level Exception: {db_err}")
        print(f"  Underlying Cause (`__cause__`): {db_err.__cause__!r}")


if __name__ == "__main__":
    main()
