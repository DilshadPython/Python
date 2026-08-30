# from typing import List: Imports the List type hint container from Python's built-in typing library.
# Used for explicit return type annotations (e.g., List[str] indicates a list containing string elements).
from typing import List


def reverse_string(text: str) -> str:
    """Reverses an input string using slice notation with strict type validation."""
    # Example Call: reverse_string("Python") -> Output: 'nohtyP'
    # Explanation: text[::-1] uses extended slice step -1 to reverse character order.
    
    # Step 1: Validate input type to ensure parameter 'text' is a valid Python string (str).
    if not isinstance(text, str):
        # Raise TypeError if caller passes an invalid data type (e.g., integer or list).
        raise TypeError("Input must be a string")
    
    # Step 2: Perform sequence reversing using slice step notation [start:stop:step].
    # - Empty start & stop default to the full length of the string
    # - Step -1 traverses the string backwards from the last character to the first
    return text[::-1]


def format_user_greeting(username: str, role: str = "Developer") -> str:
    """Formats a modern f-string user greeting with default values and text normalization."""
    # Example Call: format_user_greeting("  dilshad ", "Developer") -> Output: 'Welcome Dilshad (Developer)'
    # Explanation: .strip() cleans spaces, .capitalize() turns 'dilshad' into 'Dilshad', and f-string interpolates values.
    
    # Step 1: Check if username is empty or falsy.
    if not username:
        # Raise ValueError if username string is empty ("").
        raise ValueError("Username cannot be empty")
    
    # Step 2: Clean input and construct formatted string:
    # - username.strip(): Removes leading and trailing whitespace characters.
    # - .capitalize(): Converts first letter to uppercase and remaining characters to lowercase.
    # - f"Welcome {var} ({role})": Modern f-string (Python 3.6+) interpolates cleaned variables directly into text.
    return f"Welcome {username.strip().capitalize()} ({role})"


def extract_words(text: str) -> List[str]:
    """Splits text into words and cleans trailing punctuation using list comprehension."""
    # Example Call: extract_words("Hello, Python 3 world!") -> Output: ['Hello', 'Python', '3', 'world']
    # Explanation: .split() splits string on whitespace; list comprehension strips punctuation (",.!?") from each word.
    
    # Step 1: Handle empty text edge case immediately by returning an empty list.
    if not text:
        return []
    
    # Step 2: Tokenize and clean words:
    # - text.split(): Breaks sentence string into raw token list delimited by any whitespace (spaces/tabs/newlines).
    # - word.strip(",.!?"): Strips leading/trailing punctuation characters from each individual token.
    # - if word.strip(): Filters out any tokens that become completely empty after stripping punctuation.
    # - [ ... for word in ... ]: List comprehension builds and returns clean List[str].
    return [word.strip(",.!?") for word in text.split() if word.strip()]

