"""
Custom Object __reversed__() Protocol & Sequence Fallback Module.

This module demonstrates how custom Python classes support built-in reversed():
- Primary Protocol Hook: Defining __reversed__(self) method returning a custom iterator
- Fallback Sequence Protocol: Defining __len__(self) and __getitem__(self, index)
- Comparing custom __reversed__ protocol execution against sequence index lookup
"""
# "from typing import Iterator, List, Any" imports type hint symbols.
from typing import Iterator, List, Any


class CustomReversibleContainer:
    """
    A custom class implementing the explicit __reversed__() protocol hook (PEP 322).
    """

    def __init__(self, elements: List[Any]) -> None:
        self.elements = list(elements)

    def __reversed__(self) -> Iterator[Any]:
        """
        Custom iterator hook invoked by built-in reversed(obj).

        Returns:
            Iterator[Any]: Generator yielding elements in reverse order.
        """
        for item in reversed(self.elements):
            yield item

    def __len__(self) -> int:
        return len(self.elements)

    def __getitem__(self, index: int) -> Any:
        return self.elements[index]


class SequenceFallbackContainer:
    """
    A class that does NOT implement __reversed__(), but relies on Python's sequence fallback
    using __len__() and __getitem__() for reversed(obj).
    """

    def __init__(self, elements: List[Any]) -> None:
        self.elements = list(elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __getitem__(self, index: int) -> Any:
        return self.elements[index]


def demonstrate_custom_reversed_protocol(items: List[Any]) -> List[Any]:
    """
    Pass a CustomReversibleContainer instance to built-in reversed().

    Args:
        items (List[Any]): List of elements.

    Returns:
        List[Any]: Reversed items produced via __reversed__() protocol hook.
    """
    container = CustomReversibleContainer(items)
    return list(reversed(container))


def demonstrate_sequence_fallback_protocol(items: List[Any]) -> List[Any]:
    """
    Pass a SequenceFallbackContainer instance to built-in reversed().

    Python automatically uses range(len(obj) - 1, -1, -1) and calls obj[i] under the hood.

    Args:
        items (List[Any]): List of elements.

    Returns:
        List[Any]: Reversed items produced via fallback sequence indexing.
    """
    container = SequenceFallbackContainer(items)
    return list(reversed(container))


if __name__ == "__main__":
    print("=== Step 2: Custom __reversed__ Protocol & Fallback ===")
    sample = ["Alpha", "Beta", "Gamma", "Delta"]

    custom_res = demonstrate_custom_reversed_protocol(sample)
    print(f"Custom __reversed__() hook output : {custom_res}")

    fallback_res = demonstrate_sequence_fallback_protocol(sample)
    print(f"Fallback __len__/__getitem__ output: {fallback_res}")
