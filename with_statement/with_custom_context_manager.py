"""
Class-Based Custom Context Manager Protocol Module.

This module demonstrates building custom class-based context managers implementing
__enter__() setup and __exit__() teardown lifecycle protocols.
"""
# "from typing import Optional, Type, Any" imports typing annotations.
# Optional[T] allows specifying arguments that can be T or None.
# Type[BaseException] specifies exception class types passed to __exit__.
from typing import Any, Optional, Type


class StudentContextManager:
    """
    Custom context manager demonstrating __enter__ setup and __exit__ teardown.
    """

    def __enter__(self) -> "StudentContextManager":
        """
        Execute context setup operations and return context target object.

        Returns:
            StudentContextManager: Self instance reference.
        """
        print('Entering "with" context block.')
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> Optional[bool]:
        """
        Execute context cleanup and resource release operations.
        """
        print('Leaving "with" context block.')
        return None

    def text_msg(self) -> str:
        """
        Return instance memory identity message.

        Returns:
            str: Instance greeting string.
        """
        return f"Hi from StudentContextManager instance id: {id(self)}"


def run_student_context() -> str:
    """
    Execute StudentContextManager within a with statement block.

    Returns:
        str: Resulting message string.
    """
    msg = ""
    with StudentContextManager() as obj:
        msg = obj.text_msg()
        print(msg)
    return msg


if __name__ == "__main__":
    print("=== Custom StudentContextManager Demonstration ===")
    result = run_student_context()
    print(f"Context execution completed: {result}")
