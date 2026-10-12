"""
Context Manager Exception Handling Module.

This module demonstrates exception inspection and suppression logic inside __exit__() context manager methods.
"""
# "from typing import Any, Optional, Tuple, Type" imports type hint symbols.
# Any allows arbitrary parameter types, Optional[T] handles T or None, Tuple specifies return pairs,
# and Type[BaseException] annotations represent exception class types.
from typing import Any, Optional, Tuple, Type


class StudentExceptionContextManager:
    """
    Context manager inspecting exception parameters and handling runtime errors inside __exit__.
    """

    def __init__(self, suppress_errors: bool = True) -> None:
        """
        Initialize context manager with error suppression preference.

        Args:
            suppress_errors (bool): If True, suppresses caught exceptions by returning True from __exit__.
        """
        self.suppress_errors = suppress_errors
        self.last_error_type: Optional[str] = None

    def __enter__(self) -> "StudentExceptionContextManager":
        """
        Initialize context setup.

        Returns:
            StudentExceptionContextManager: Self instance reference.
        """
        print('Entering exception-aware "with" block.')
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> bool:
        """
        Log exception details and optionally return True to suppress exception propagation.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception class type.
            exc_val (Optional[BaseException]): Exception instance value.
            exc_tb (Optional[Any]): Traceback object.

        Returns:
            bool: True if exception is suppressed, False otherwise.
        """
        if exc_type is not None:
            self.last_error_type = exc_type.__name__
            print(f"Caught Error Type: {exc_type}")
            print(f"Caught Error Value: {exc_val}")
            print(f"Caught Error Traceback: {exc_tb}")
            # Returning True suppresses the exception from propagating outside the 'with' block
            return self.suppress_errors

        print('Leaving "with" block cleanly with zero exceptions.')
        return False

    def text_msg(self, name: str) -> str:
        """
        Format greeting message with provided name.

        Args:
            name (str): Person name.

        Returns:
            str: Formatted message.
        """
        return f"Hi {name}, instance id: {id(self)}"


def run_exception_context(
    name: str = "Dilshad", trigger_error: bool = False
) -> Tuple[bool, Optional[str]]:
    """
    Execute exception-handling context manager with optional error triggering.

    Args:
        name (str): Person name. Defaults to "Dilshad".
        trigger_error (bool): If True, raises a ValueError inside context suite.

    Returns:
        Tuple[bool, Optional[str]]: Pair of (executed_cleanly, last_error_type).
    """
    manager = StudentExceptionContextManager(suppress_errors=True)
    executed_cleanly = False

    with manager as obj:
        print(obj.text_msg(name))
        if trigger_error:
            raise ValueError("Simulated error inside context block")
        executed_cleanly = True

    return executed_cleanly, manager.last_error_type


if __name__ == "__main__":
    print("=== Exception Handling Context Manager Demonstration ===")
    clean, err = run_exception_context("Dilshad", trigger_error=False)
    print(f"Clean run: {clean}, Error caught: {err}\n")

    clean_err, err_type = run_exception_context("Dilshad", trigger_error=True)
    print(f"Suppressed error run: {clean_err}, Error caught: {err_type}")
