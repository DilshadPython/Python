"""
Interactive String Unpacking & Wildcard Discard (`unpack.py`).

Demonstrates string split unpacking into variables with wildcard placeholder (`_`) to ignore
unneeded elements.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from beginner_unpacking import demonstrate_wildcard_discard`: Discard helper.
# =========================================================================
try:
    from unpacking.beginner_unpacking import demonstrate_wildcard_discard
except ImportError:
    from beginner_unpacking import demonstrate_wildcard_discard


def process_user_name(name_input: str) -> str:
    """Extract first name using wildcard discard (`_`)."""
    return demonstrate_wildcard_discard(name_input)


def main() -> None:
    """Prompt user for full name and unpack first name."""
    try:
        user_input = input("What is your name? ")
        fname = process_user_name(user_input)
        print(f"Welcome back, {fname}!")
    except ValueError as error:
        print("ValueError: Please enter at least two words (first and last name).", error)


if __name__ == "__main__":
    main()
