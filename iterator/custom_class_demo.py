"""
Custom Class Iterator Demonstration Script.

This script demonstrates defining custom classes that implement Python's Iterator protocol (__iter__ and __next__).
"""
# "from typing import List, Iterator" imports type hint symbols.
from typing import List, Iterator


class AlphabetIterator:
    """
    A custom class that iterates through uppercase letters of the alphabet.
    """

    def __init__(self) -> None:
        self.char_list: List[str] = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        self.index: int = 0

    def __iter__(self) -> Iterator[str]:
        """Return the iterator instance itself."""
        return self

    def __next__(self) -> str:
        """Fetch the next character or raise StopIteration when exhausted."""
        if self.index >= len(self.char_list):
            raise StopIteration("End of alphabet list reached.")

        current_char = self.char_list[self.index]
        self.index += 1
        return current_char


if __name__ == "__main__":
    print("=== Custom Alphabet Iterator Demonstration ===")
    alphabet_obj = AlphabetIterator()
    my_iter = iter(alphabet_obj)

    print("Manual next() calls:")
    print(f"  Item 1: {next(my_iter)}")
    print(f"  Item 2: {next(my_iter)}")
    print(f"  Item 3: {next(my_iter)}")

    print("\nLooping through remaining items:")
    for char in my_iter:
        print(char, end=" ")
    print()
