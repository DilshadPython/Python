"""Max Size List Demonstration Module.

This module demonstrates designing a bounded list container (`MaxSizeList`) that encapsulates state
per instance (`self.inner_list`) and enforces a fixed maximum capacity by evicting oldest elements.
"""

from typing import List, Any


class MaxSizeList:
    """Class maintaining a list of items up to a maximum size capacity."""

    def __init__(self, max_size: int) -> None:
        """Initialize MaxSizeList with maximum capacity.

        Args:
            max_size: Maximum number of elements allowed in list.
        """
        self.max_size: int = max_size
        self.inner_list: List[Any] = []

    def push(self, item: Any) -> None:
        """Append item to list, evicting the oldest element if capacity is exceeded.

        Args:
            item: Item to add.
        """
        self.inner_list.append(item)
        if len(self.inner_list) > self.max_size:
            self.inner_list.pop(0)

    def get_list(self) -> List[Any]:
        """Return copy of current list elements.

        Returns:
            List of stored items.
        """
        return list(self.inner_list)


if __name__ == "__main__":
    print("=== Max Size List Demonstration ===")
    list_a = MaxSizeList(4)
    list_b = MaxSizeList(2)

    for lang in ["Python", "Java", "C++", "JavaScript"]:
        list_a.push(lang)

    for item in ["A", "B", "C", "D", "E", "F"]:
        list_b.push(item)

    print("List A (max 4):", list_a.get_list())
    print("List B (max 2, evicted old items):", list_b.get_list())
