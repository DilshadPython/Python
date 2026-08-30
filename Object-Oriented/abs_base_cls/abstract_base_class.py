"""Abstract Base Class Demonstration Module.

This module demonstrates creating Abstract Base Classes (ABCs) in Python using the `abc` module.
It details how inheriting from `abc.ABC` and using `@abc.abstractmethod` prevents direct object instantiation
and enforces abstract method implementation in derived subclasses.
"""

# "import abc" imports Python's standard Abstract Base Class library.
import abc
from typing import Any


class GetterSetter(abc.ABC):
    """Abstract Base Class defining a contract for getting and setting values."""

    @abc.abstractmethod
    def set_val(self, value: Any) -> None:
        """Abstract method to set a value. Must be overridden by concrete subclasses."""
        pass

    @abc.abstractmethod
    def get_val(self) -> Any:
        """Abstract method to retrieve a value. Must be overridden by concrete subclasses."""
        pass


class ValueContainer(GetterSetter):
    """Concrete subclass implementing the GetterSetter abstract contract."""

    def __init__(self, initial_value: Any = None) -> None:
        """Initialize ValueContainer with an optional initial value."""
        self._val: Any = initial_value

    def set_val(self, value: Any) -> None:
        """Set a value in the container instance.

        Args:
            value: Value to store.
        """
        self._val = value

    def get_val(self) -> Any:
        """Retrieve and return stored value.

        Returns:
            Stored value.
        """
        return self._val


if __name__ == "__main__":
    print("=== Abstract Base Class Demonstration ===")
    
    try:
        # Attempting to instantiate an ABC raises TypeError
        abstract_obj = GetterSetter()  # type: ignore
    except TypeError as err:
        print("Expected Error on ABC instantiation:", err)

    container = ValueContainer(100)
    print("Initial Value:", container.get_val())
    container.set_val(250)
    print("Updated Value:", container.get_val())
