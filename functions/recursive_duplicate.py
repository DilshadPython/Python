"""
Demonstrates recursive string deduplication removing consecutive duplicate characters.
"""


def remove_duplicate(text: str) -> str:
    """Recursively remove adjacent identical characters from a string."""
    if len(text) <= 1:
        return text

    if text[0] == text[1]:
        return remove_duplicate(text[1:])
    
    return text[0] + remove_duplicate(text[1:])


# Backwards compatibility function name
remove_duplecate = remove_duplicate


if __name__ == "__main__":
    sample = "Pyythhoon"
    result = remove_duplicate(sample)
    print(f"Original: {sample} -> Deduplicated: {result}")
