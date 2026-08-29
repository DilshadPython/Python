"""Structural Pattern Matching Wildcard Case ('case _:') Default Fallback.

Demonstrates handling unknown or unmatched cases using the underscore wildcard
'case _:' in Python 3.10+ match statements.

Import Notes:
    - 'import sys': Used to detect Python runtime version and execute pattern matching
      in Python 3.10+ or fall back to dictionary mapping in Python 3.3–3.9.
    - 'from typing import List': Standard library typing import for list annotations.
"""

import sys
from typing import List


def classify_team_with_fallback(team_name: str) -> str:
    """Classify sports teams and provide explicit fallback message for unknown teams."""
    cleaned_name = team_name.strip()

    if sys.version_info >= (3, 10):
        match cleaned_name:
            case "Manchester":
                return "English Team"
            case "Real Madrid":
                return "Spanish Team"
            case "Roma":
                return "Italian Team"
            case "Bayern Munich":
                return "German Team"
            case "Los Angeles":
                return "Non-EU Team"
            case _:
                # Wildcard pattern matches any value not caught by preceding cases
                return f"Team '{cleaned_name}' does not exist in the database. Please try again."
    else:
        mapping = {
            "Manchester": "English Team",
            "Real Madrid": "Spanish Team",
            "Roma": "Italian Team",
            "Bayern Munich": "German Team",
            "Los Angeles": "Non-EU Team",
        }
        return mapping.get(cleaned_name, f"Team '{cleaned_name}' does not exist in the database. Please try again.")


def demo_not_match() -> None:
    """Run wildcard pattern matching demonstration."""
    test_teams: List[str] = ["Real Madrid", "Paris Saint-Germain", "Unknown FC"]
    for team in test_teams:
        result = classify_team_with_fallback(team)
        print(f"Query: '{team:20s}' -> {result}")


if __name__ == "__main__":
    demo_not_match()