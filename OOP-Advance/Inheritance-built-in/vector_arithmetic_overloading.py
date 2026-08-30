"""Vector Arithmetic Operator Overloading Module.

This module demonstrates overloading arithmetic operators (`__add__`, `__sub__`) and string representation (`__repr__`)
to perform element-wise addition and subtraction on custom list wrapper objects (`SumList`).
"""

from typing import List, Any


class SumList:
    """Custom sequence wrapper providing element-wise addition and subtraction operators."""

    def __init__(self, items: List[int]) -> None:
        """Initialize SumList with list of integer elements.

        Args:
            items: List of integers.
        """
        self.mylist: List[int] = list(items)

    def __add__(self, other: "SumList") -> "SumList":
        """Overload addition (+) operator to add corresponding list elements pairwise.

        Args:
            other: Another SumList instance.

        Returns:
            New SumList instance containing pairwise element sums.
        """
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __sub__(self, other: "SumList") -> "SumList":
        """Overload subtraction (-) operator to subtract corresponding list elements pairwise.

        Args:
            other: Another SumList instance.

        Returns:
            New SumList instance containing pairwise element differences.
        """
        new_list = [x - y for x, y in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __repr__(self) -> str:
        """Return string representation of internal list."""
        return str(self.mylist)


if __name__ == "__main__":
    print("=== Vector Arithmetic Operator Overloading ===")

    obj1 = SumList([10, 11, 22, 33, 41])
    obj2 = SumList([80, 121, 20, 300, 50])

    print("List 1:", obj1)
    print("List 2:", obj2)

    added_obj = obj1 + obj2
    print("Pairwise Sum (obj1 + obj2):", added_obj)

    subtracted_obj = obj1 - obj2
    print("Pairwise Difference (obj1 - obj2):", subtracted_obj)
