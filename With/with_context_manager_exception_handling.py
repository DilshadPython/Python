"""
Demonstrates exception inspection and suppression logic inside __exit__ context manager methods.
"""
from typing import Any, Optional, Tuple, Type


class StudentExceptionContextManager:
    """Context manager inspecting exception parameters and handling runtime errors."""

    def __init__(self, suppress_errors: bool = True) -> None:
        self.suppress_errors = suppress_errors
        self.last_error_type: Optional[str] = None

    def __enter__(self) -> 'StudentExceptionContextManager':
        """Initialize context setup."""
        print('Entering exception-aware "with" block.')
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any]
    ) -> bool:
        """Log exception details and optionally return True to suppress exception propagation."""
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
        """Format greeting message with provided name."""
        return f"Hi {name}, instance id: {id(self)}"


def run_exception_context(name: str = "Dilshad", trigger_error: bool = False) -> Tuple[bool, Optional[str]]:
    """Execute exception-handling context manager with optional error triggering."""
    manager = StudentExceptionContextManager(suppress_errors=True)
    executed_cleanly = False

    with manager as obj:
        print(obj.text_msg(name))
        if trigger_error:
            raise ValueError("Simulated error inside context block")
        executed_cleanly = True

    return executed_cleanly, manager.last_error_type


if __name__ == '__main__':
    clean, err = run_exception_context("Dilshad", trigger_error=False)
    print(f"Clean run: {clean}, Error caught: {err}")

    clean_err, err_type = run_exception_context("Dilshad", trigger_error=True)
    print(f"Suppressed error run: {clean_err}, Error caught: {err_type}")
