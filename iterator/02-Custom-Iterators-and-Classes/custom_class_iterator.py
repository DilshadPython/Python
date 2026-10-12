"""
Custom Class Iterator Module.

This module demonstrates building user-defined custom iterators in Python:
- Implementing the Iterator Protocol: Defining __iter__() and __next__() dunder methods
- Managing stateful instance attributes during iteration
- Raising StopIteration when boundaries are reached
"""
# "from typing import List, Iterator, Any" imports type hint annotations.
from typing import List, Iterator, Any


class AlphabetIterator:
    """
    A custom iterator that iterates through uppercase letters of the alphabet.

    Implements both __iter__() (returning self) and __next__() (returning character or raising StopIteration).
    """

    def __init__(self, char_limit: int = 26) -> None:
        """
        Initialize the AlphabetIterator with a character limit.

        Args:
            char_limit (int): Number of characters to iterate (1 to 26). Defaults to 26.
        """
        all_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.char_list: List[str] = all_chars[:min(max(1, char_limit), 26)]
        self.index: int = 0

    def __iter__(self) -> Iterator[str]:
        """
        Return the iterator instance itself.

        Returns:
            Iterator[str]: Self reference.
        """
        return self

    def __next__(self) -> str:
        """
        Fetch the next character or raise StopIteration.

        Returns:
            str: Next uppercase letter.

        Raises:
            StopIteration: When index exceeds char_list length.
        """
        if self.index >= len(self.char_list):
            raise StopIteration("End of alphabet characters reached.")

        current_char = self.char_list[self.index]
        self.index += 1
        return current_char


class BoundedFibonacciIterator:
    """
    A custom stateful iterator generating Fibonacci numbers up to a maximum value.
    """

    def __init__(self, max_value: int) -> None:
        """
        Args:
            max_value (int): Maximum Fibonacci number cap.
        """
        self.max_value = max_value
        self.a: int = 0
        self.b: int = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.a > self.max_value:
            raise StopIteration("Fibonacci max value threshold reached.")

        curr = self.a
        self.a, self.b = self.b, self.a + self.b
        return curr


def collect_alphabet_sequence(limit: int = 5) -> List[str]:
    """
    Collect items from AlphabetIterator using built-in iter() and for loop.

    Args:
        limit (int): Character limit.

    Returns:
        List[str]: List of collected characters.
    """
    alphabet_iter = AlphabetIterator(char_limit=limit)
    return list(alphabet_iter)


def collect_fibonacci_sequence(max_val: int = 50) -> List[int]:
    """
    Collect items from BoundedFibonacciIterator.

    Args:
        max_val (int): Upper bound value limit.

    Returns:
        List[int]: List of Fibonacci numbers.
    """
    fib_iter = BoundedFibonacciIterator(max_value=max_val)
    return list(fib_iter)


if __name__ == "__main__":
    print("=== Step 2: Custom Class Iterators ===")
    alphabet = collect_alphabet_sequence(8)
    print(f"AlphabetIterator (limit=8) : {alphabet}")

    fib_seq = collect_fibonacci_sequence(50)
    print(f"BoundedFibonacciIterator (max=50) : {fib_seq}")
