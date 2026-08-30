"""Abstract Inheritance Demonstration Module.

This module demonstrates advanced Abstract Base Class inheritance patterns:
concrete base implementations, input type validation in derived subclasses (`GetSetInt`),
and value history tracking (`GetSetList`).
"""

import abc
from typing import List, Any


class GetSetParent(abc.ABC):
    """Abstract Base Class providing a common base state and requiring a doc string method."""

    def __init__(self, value: Any = 0) -> None:
        """Initialize base state."""
        self.val: Any = value

    def set_val(self, value: Any) -> None:
        """Set stored value in base instance.

        Args:
            value: Input value.
        """
        self.val = value

    def get_val(self) -> Any:
        """Retrieve stored value from base instance.

        Returns:
            Stored value.
        """
        return self.val

    @abc.abstractmethod
    def show_docs(self) -> str:
        """Abstract method returning documentation details for the subclass."""
        pass


class GetSetInt(GetSetParent):
    """Concrete subclass restricting set values strictly to integer types."""

    def set_val(self, value: Any) -> None:
        """Set value, falling back to 0 if input is not an integer.

        Args:
            value: Integer value to store.
        """
        validated_val = value if isinstance(value, int) else 0
        super().set_val(validated_val)

    def show_docs(self) -> str:
        """Return documentation string specifying integer restriction."""
        return f"GetSetInt instance (id={id(self)}): accepts strictly integer values."


class GetSetList(GetSetParent):
    """Concrete subclass recording a history of all set values in a list."""

    def __init__(self, initial_value: Any = 0) -> None:
        """Initialize value history list with initial value."""
        super().__init__(initial_value)
        self.val_history: List[Any] = [initial_value]

    def set_val(self, value: Any) -> None:
        """Append value to history list and set current value.

        Args:
            value: Value to append.
        """
        self.val_history.append(value)
        super().set_val(value)

    def get_val(self) -> Any:
        """Return the most recent value set (last element in history).

        Returns:
            Most recent value.
        """
        return self.val_history[-1]

    def get_vals(self) -> List[Any]:
        """Return complete history of set values.

        Returns:
            List of all values recorded.
        """
        return self.val_history

    def show_docs(self) -> str:
        """Return documentation string specifying history length."""
        return f"GetSetList instance: recorded {len(self.val_history)} values in history."


if __name__ == "__main__":
    print("=== Abstract Inheritance Demonstration ===")

    gsi = GetSetInt(9)
    gsi.set_val(7)
    print("GetSetInt Current Value:", gsi.get_val())
    print(gsi.show_docs())

    gsl = GetSetList(6)
    gsl.set_val(99)
    gsl.set_val(3)
    gsl.set_val(49)
    print("\nGetSetList Most Recent Value:", gsl.get_val())
    print("GetSetList History:", gsl.get_vals())
    print(gsl.show_docs())
