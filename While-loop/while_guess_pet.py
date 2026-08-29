"""
Demonstrates pet name guessing game logic with while loops and conditional validation.
"""
from typing import List, Tuple


def guess_pet_name(answers: List[str]) -> Tuple[bool, int]:
    """Process pet name guess attempts until correct answer 'Raffi' is found."""
    attempts = 0
    for ans in answers:
        attempts += 1
        if ans.strip() == "Raffi":
            return True, attempts
    return False, attempts


if __name__ == '__main__':
    found, count = guess_pet_name(["Rex", "Raffi"])
    print(f"Guess status: {found} after {count} attempts.")
