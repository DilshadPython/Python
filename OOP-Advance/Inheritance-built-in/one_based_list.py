"""One-Based Index List Subclass Demonstration Module.

This module demonstrates inheriting from the built-in `list` class to implement
a 1-based indexing sequence (`MyList`) by overriding `__getitem__` and `__setitem__`.
Accessing `obj[1]` returns index 0 of the underlying list.
"""

from typing import Any


class MyList(list):
    """Subclass of list translating 1-based index access to internal 0-based indices."""

    def __getitem__(self, index: int) -> Any:
        """Get element using 1-based index.

        Args:
            index: 1-based index integer.

        Returns:
            Element at internal index (index - 1).

        Raises:
            IndexError: If index is 0 or negative.
        """
        if index <= 0:
            raise IndexError("MyList indices start at 1 (0 or negative indices are invalid).")
        return list.__getitem__(self, index - 1)

    def __setitem__(self, index: int, value: Any) -> None:
        """Set element using 1-based index.

        Args:
            index: 1-based index integer.
            value: Value to assign.

        Raises:
            IndexError: If index is 0 or negative.
        """
        if index <= 0:
            raise IndexError("MyList indices start at 1 (0 or negative indices are invalid).")
        list.__setitem__(self, index - 1, value)


if __name__ == "__main__":
    print("=== One-Based Index List Subclass Demonstration ===")

    obj = MyList(["ABc", "DEf", "GEh", "IJk"])
    print("Full List Contents:", obj)

    obj.append("LMn")
    print("List Contents After Append:", obj)

    print("Element at Index 1 (obj[1]):", obj[1])
    print("Element at Index 4 (obj[4]):", obj[4])

    obj[1] = "UPDATED_FIRST"
    print("Updated Element at Index 1:", obj[1])
