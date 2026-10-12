"""
Demonstrates multi-choice quiz evaluation logic using a while loop.
"""
from typing import List, Tuple


def quiz_company(guesses: List[int]) -> Tuple[bool, str]:
    """Evaluate company quiz choices within a maximum of 3 attempts."""
    attempts = 0
    for guess in guesses:
        attempts += 1
        if guess == 1:
            return True, "Correct! The company is Google."
        elif guess == 3:
            return False, "Sorry, your guess was wrong. The answer was Google."
        else:
            if attempts >= 3:
                return False, "Maximum attempts reached."
    return False, "No correct choice provided."


if __name__ == '__main__':
    success, msg = quiz_company([2, 1])
    print(f"Quiz Result: {msg}")
