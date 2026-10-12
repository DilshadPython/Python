"""
Demonstrates recursive string expansion inserting spaces between adjacent characters.
"""


def recursive_explode(text: str) -> str:
    """Recursively insert single space characters between letters in a string."""
    if len(text) <= 1:
        return text

    return text[0] + " " + recursive_explode(text[1:])


if __name__ == "__main__":
    sample = "Python"
    exploded = recursive_explode(sample)
    print(f"Exploded: '{exploded}'")
