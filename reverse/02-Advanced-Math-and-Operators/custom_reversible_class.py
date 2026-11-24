# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - from typing import Any, Dict, List, Iterator, Sequence: Type hint definitions.
# =========================================================================
from typing import Any, Dict, List, Iterator, Sequence


class CountdownSequence:
    """
    Custom sequence class implementing the __reversed__() dunder protocol.
    
    When passed to built-in reversed(), CPython inspects the object for __reversed__().
    If present, reversed(obj) invokes obj.__reversed__() directly.
    """
    def __init__(self, start: int, end: int) -> None:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end bounds must be integers.")
        self.start: int = start
        self.end: int = end
        self.items: List[int] = list(range(start, end + 1))

    def __iter__(self) -> Iterator[int]:
        """Standard forward iteration protocol."""
        return iter(self.items)

    def __reversed__(self) -> Iterator[int]:
        """Custom reverse iteration protocol hook."""
        for item in reversed(self.items):
            yield item * 10  # Apply custom transform during reverse traversal


class LegacySequence:
    """
    Custom sequence class implementing sequence protocol (__len__ and __getitem__).
    
    When __reversed__() is NOT defined, CPython falls back to calling __len__()
    and indexing backwards via __getitem__(i) from len-1 down to 0.
    """
    def __init__(self, elements: List[Any]) -> None:
        self._elements: List[Any] = list(elements)

    def __len__(self) -> int:
        """Returns sequence length."""
        return len(self._elements)

    def __getitem__(self, index: int) -> Any:
        """Retrieves item by index."""
        return self._elements[index]


def demonstrate_custom_reversible_objects() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> custom_reversible_class.py]
    Demonstrates custom class reversing via __reversed__() hook vs fallback sequence protocol.

    Returns:
        Dict[str, Any]: Results of forward and custom reverse iteration.
    """
    # 1. Custom class with explicit __reversed__() hook
    cd = CountdownSequence(1, 5)
    forward_cd = list(cd)             # [1, 2, 3, 4, 5]
    reversed_cd = list(reversed(cd))  # [50, 40, 30, 20, 10] due to custom transform

    # 2. Legacy class relying on __len__ and __getitem__ fallback
    leg = LegacySequence(["alpha", "beta", "gamma"])
    forward_leg = [leg[i] for i in range(len(leg))]  # ["alpha", "beta", "gamma"]
    reversed_leg = list(reversed(leg))                # ["gamma", "beta", "alpha"]

    return {
        "forward_countdown": forward_cd,
        "custom_reversed_countdown": reversed_cd,
        "forward_legacy": forward_leg,
        "fallback_reversed_legacy": reversed_leg,
    }


if __name__ == "__main__":
    print(demonstrate_custom_reversible_objects())
