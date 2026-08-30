"""Legacy Books Script (Refactored).

This module updates the original `books.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed book encapsulation, see `book_instance.py`.
"""

from book_instance import Book


if __name__ == "__main__":
    print("=== Legacy Books (Refactored) ===")
    obj_1 = Book("Data Science", 20.0, "Martin Schulter")
    obj_2 = Book("Computer Science", 39.0, "Tomas Adam")
    print("Cost 1:", obj_1.cost)
    print("Owner 1:", obj_1.owner)
