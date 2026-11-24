"""Calculate average scores using variable positional arguments (*args).

This module demonstrates calculating statistical averages with flexible
input counts, including graceful handling for empty inputs.
"""

from typing import Union

Number = Union[int, float]


def average_score(*scores: Number) -> float:
    """Calculate the arithmetic mean of variable score arguments.

    Args:
        *scores: Arbitrary number of numerical scores (int or float).

    Returns:
        float: The average of the scores, or 0.0 if no scores are passed.
    """
    if not scores:
        return 0.0
    return float(sum(scores) / len(scores))


# Backward-compatible alias for previous naming convention
avarage_score = average_score


if __name__ == "__main__":
    print(f"Average of (66, 74, 85, 89): {average_score(66, 74, 85, 89):.2f}")
    print(f"Average of (95, 84, 71, 89, 69): {average_score(95, 84, 71, 89, 69):.2f}")
    print(f"Average with no arguments: {average_score()}")
