"""Multi-Branch Selection Logic with 'if-elif-else'.

Demonstrates cascading conditional structures for multi-range value categorization,
such as academic grading systems and ambient temperature conditions.

Import Notes:
    - 'import sys': Used to query Python environment details.
    - 'from typing import List, Tuple': Used for explicit static typing.
"""

import sys
from typing import List, Tuple


def evaluate_grade(score: float) -> str:
    """Evaluate an academic numerical score into a letter grade classification.
    
    Raises:
        ValueError: If score is outside the valid percentage range [0.0, 100.0].
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive.")
    
    if score >= 90:
        return "Grade A (Excellent)"
    elif score >= 80:
        return "Grade B (Good)"
    elif score >= 70:
        return "Grade C (Satisfactory)"
    elif score >= 60:
        return "Grade D (Pass)"
    else:
        return "Grade F (Fail)"


def classify_temperature(celsius_temp: float) -> str:
    """Classify weather conditions based on temperature in degrees Celsius."""
    if celsius_temp >= 35:
        return "Extreme Heat"
    elif celsius_temp >= 25:
        return "Warm / Summer"
    elif celsius_temp >= 15:
        return "Mild / Pleasant"
    elif celsius_temp >= 0:
        return "Cold / Freezing Point"
    else:
        return "Sub-Zero / Below Freezing"


def demo_elif() -> None:
    """Run interactive demonstration of elif branching logic."""
    sample_scores: List[float] = [95.5, 83.0, 72.0, 64.0, 45.0]
    print(f"--- Academic Score Evaluation (Python {sys.version_info.major}.{sys.version_info.minor}) ---")
    for score in sample_scores:
        print(f"Score {score:5.1f} -> {evaluate_grade(score)}")

    print("\n--- Temperature Condition Classification ---")
    sample_temps: List[float] = [38.0, 27.0, 18.0, 5.0, -8.0]
    for temp in sample_temps:
        print(f"Temperature {temp:5.1f}°C -> {classify_temperature(temp)}")


if __name__ == "__main__":
    demo_elif()
