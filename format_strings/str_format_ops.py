"""str.format() Method Operations Module.

Provides functions demonstrating advanced string formatting using Python's `str.format()`
method, positional/keyword arguments, sequence indexing, object attribute access,
alignment, and number specifiers.
"""

from typing import Any, Sequence, Union


def format_positional_and_keyword(
    name: str,
    age: int,
    city: str = "London",
) -> str:
    """Format strings using positional `{0}` and keyword `{key}` placeholders.

    Args:
        name: Name string.
        age: Age integer.
        city: City string.

    Returns:
        Formatted string combining positional and named placeholders.
    """
    pattern = "Hello {0}! You are {1} years old and live in {city}."
    return pattern.format(name, age, city=city)


def format_index_and_attribute(pos_data: Sequence[Any], target_object: Any) -> str:
    """Format strings by indexing tuples/lists `{pos[0]}` and accessing object attributes `{obj.attr}`.

    Args:
        pos_data: Sequence object (tuple or list).
        target_object: Object containing attributes.

    Returns:
        Formatted string containing accessed indices and properties.
    """
    pattern = "User age={pos[0]}, height={pos[1]}cm | Object attribute: pi={obj.pi}"
    return pattern.format(pos=pos_data, obj=target_object)


def format_alignment_and_padding(
    text: str,
    width: int = 20,
    align_char: str = "^",
    fill_char: str = "-",
) -> str:
    """Align text within a specified width using `<` (left), `>` (right), or `^` (center).

    Args:
        text: Text string to align.
        width: Minimum container width.
        align_char: Alignment specifier ('<', '>', '^').
        fill_char: Padding character.

    Returns:
        Padded and aligned string.
    """
    format_spec = "{:" + fill_char + align_char + str(width) + "}"
    return format_spec.format(text)


def format_number_commas_and_percents(amount: float) -> str:
    """Format numbers with thousand separators `,` and percentage `%`.

    Args:
        amount: Floating point numeric value.

    Returns:
        Formatted string with comma separators and percentage notation.
    """
    currency_str = "${:,.2f}".format(amount)
    percentage_str = "{:.1%}".format(amount / 100)
    return f"Currency: {currency_str} | Percentage: {percentage_str}"


def main() -> None:
    """Demonstrate `str.format()` operations."""
    print("--- str.format() Operations ---")

    # 1. Positional & Keyword
    print(format_positional_and_keyword("Dilshad", 30, city="London"))

    # 2. Index & Attribute access
    import math

    person_data = (30, 175, "01/03/1975")
    print(format_index_and_attribute(person_data, math))

    # 3. Alignment & Padding
    print(f"\nLeft aligned:   '{format_alignment_and_padding('Python', 20, '<', ' ')}'")
    print(f"Center aligned: '{format_alignment_and_padding('Python', 20, '^', '=')}'")
    print(f"Right aligned:  '{format_alignment_and_padding('Python', 20, '>', '*')}'")

    # 4. Currency and percentage
    print(f"\n{format_number_commas_and_percents(1234567.89)}")


if __name__ == "__main__":
    main()
