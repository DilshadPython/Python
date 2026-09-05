"""
Python Exception Handling: Multiple Exception Clauses & Tuples

This module demonstrates handling multiple exception types, both by grouping
exceptions into tuples `except (TypeError, ValueError):` and by defining distinct
`except` blocks for tailored handling.

Key Concepts:
- Grouping: `except (IndexError, ValueError):` traps both exception types in one block.
- Distinct Handling: Multiple `except` branches execute the first matching handler.
"""
from typing import List, Tuple, Union


def parse_and_divide(values: List[str], index1: int, index2: int) -> Union[float, str]:
    """
    Retrieves two string elements from a list, converts them to floats, and divides them.
    Catches IndexError, ValueError, and ZeroDivisionError distinctly.

    Args:
        values (List[str]): List of string representations of numbers.
        index1 (int): Index of numerator.
        index2 (int): Index of denominator.

    Returns:
        Union[float, str]: Result of division or descriptive error message.
    """
    try:
        raw1 = values[index1]
        raw2 = values[index2]
        num1 = float(raw1)
        num2 = float(raw2)
        return num1 / num2
    except IndexError:
        return f"IndexError: Invalid index provided ({index1} or {index2})."
    except ValueError:
        return f"ValueError: Element cannot be parsed as a float."
    except ZeroDivisionError:
        return f"ZeroDivisionError: Division by zero attempted."


def process_command_args(args: List[str]) -> Tuple[bool, str]:
    """
    Processes command line arguments, catching multiple input errors using exception tuples.

    Args:
        args (List[str]): Command line arguments.

    Returns:
        Tuple[bool, str]: Success status boolean and descriptive result string.
    """
    try:
        first_arg = args[0]
        parsed_int = int(first_arg)
        return True, f"Successfully parsed command argument: {parsed_int}"
    except (IndexError, ValueError) as err:
        return False, f"InputError ({type(err).__name__}): Please provide a valid integer argument."


def main() -> None:
    """Demonstrates handling multiple exception types."""
    print("=" * 60)
    print("2. Multiple Exception Clauses & Tuple Handling")
    print("=" * 60)

    sample_data = ["10", "2", "0", "invalid"]

    # 1. Successful execution
    print(f"  Valid division [0] / [1]: {parse_and_divide(sample_data, 0, 1)}")

    # 2. Division by zero branch
    print(f"  Zero division [0] / [2]: {parse_and_divide(sample_data, 0, 2)}")

    # 3. Invalid float conversion branch
    print(f"  Parse failure [0] / [3]: {parse_and_divide(sample_data, 0, 3)}")

    # 4. Out of bounds index branch
    print(f"  Index out of bounds [0] / [10]: {parse_and_divide(sample_data, 0, 10)}")

    # 5. Tuple exception handling
    print("\n--- Tuple Exception Handling (`except (IndexError, ValueError)`) ---")
    status, msg = process_command_args([])
    print(f"  Empty args status: {status} -> {msg}")

    status_invalid, msg_invalid = process_command_args(["not_a_number"])
    print(f"  Invalid arg status: {status_invalid} -> {msg_invalid}")


if __name__ == "__main__":
    main()
