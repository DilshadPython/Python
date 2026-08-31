"""
Generator-Based Context Manager Demonstration Module.

This module demonstrates using contextlib.contextmanager to convert a generator function
into a context manager, mapping pre-yield code to __enter__ and post-yield code to __exit__.
"""
# "from contextlib import contextmanager" imports decorator for turning generator functions into context managers.
from contextlib import contextmanager
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path
# "from typing import Generator, TextIO" imports type hint annotations.
from typing import Generator, TextIO


@contextmanager
def open_text_file(filename: str, mode: str = "r") -> Generator[TextIO, None, None]:
    """
    Generator context manager for managing text file resources.

    Everything before 'yield' runs during __enter__ setup.
    Everything after 'yield' runs during __exit__ teardown.
    """
    file_handle = open(filename, mode, encoding="utf-8")
    try:
        yield file_handle
    finally:
        file_handle.close()


if __name__ == "__main__":
    print("=== Generator-Based Context Manager Demonstration ===")
    demo_file = Path(__file__).parent / "context_manager_added.txt"

    with open_text_file(str(demo_file), "w") as stream:
        stream.write(
            "Using contextlib.contextmanager decorator to convert a generator function "
            "into a context manager.\n"
        )

    print(f"Is file stream closed after context exit? {stream.closed}")
