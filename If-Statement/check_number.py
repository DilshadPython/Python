"""Number Classification and Parity Evaluation Module.

Demonstrates using 'if-elif-else' statements to evaluate numeric properties
such as sign (positive/negative/zero) and parity (even/odd).

Import Notes:
    - 'from typing import Dict, Union': Imports 'Dict' and 'Union' directly from
      the standard library 'typing' module to build type-annotated return signatures.
      Using 'from typing import ...' simplifies type hints without needing 'typing.Dict'.
"""

from typing import Dict, Union


def classify_number_sign(number: Union[int, float]) -> str:
    """Classify whether a given number is positive, negative, or zero."""
    # First branch checks if number is strictly positive
    if number > 0:
        return "Positive"
    # Second branch checks if number is strictly negative
    elif number < 0:
        return "Negative"
    # Fallback branch for zero
    else:
        return "Zero"


def check_parity(number: int) -> str:
    """Determine whether an integer is even or odd using the modulo operator (%)."""
    # Number % 2 == 0 indicates an even integer
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def analyze_number(number: int) -> Dict[str, str]:
    """Perform comprehensive analysis of an integer's sign and parity."""
    number_sign = classify_number_sign(number)
    number_parity = check_parity(number)
    return {"sign": number_sign, "parity": number_parity}


def demo_check_number() -> None:
    """Demonstrate number classification with sample inputs."""
    test_values = [42, -7, 0]
    for val in test_values:
        analysis = analyze_number(val)
        print(f"Number {val:3d} -> Sign: {analysis['sign']:8s} | Parity: {analysis['parity']}")


if __name__ == "__main__":
    demo_check_number()
