"""Structural Pattern Matching ('match-case') - Introduced in Python 3.10 (PEP 634).

Pattern matching provides a powerful syntax for branching based on object values,
types, and structures.

Import Notes:
    - 'import sys': Used to detect Python runtime version and select 'match-case'
      or dictionary dispatch fallback for older Python runtimes (< 3.10).
    - 'from typing import List': Standard library typing import for list parameter annotations.
"""

import sys
from typing import List


def match_team_country_python310(team_name: str) -> str:
    """Classify a football/sports team by country using Python 3.10+ 'match-case'."""
    # Match statement syntax introduced in Python 3.10
    match team_name.strip():
        case "Manchester United" | "Manchester City" | "Manchester":
            return "English Premier League Team"
        case "Real Madrid" | "Barcelona":
            return "Spanish La Liga Team"
        case "Roma" | "Juventus" | "AC Milan":
            return "Italian Serie A Team"
        case "Bayern Munich":
            return "German Bundesliga Team"
        case "Los Angeles FC" | "Los Angeles":
            return "American MLS Team"
        case _:
            return "Uncategorized Team"


def match_team_country_legacy(team_name: str) -> str:
    """Dictionary dispatch fallback for Python 3.3 - 3.9 (Before 'match-case' existed)."""
    teams_map = {
        "Manchester": "English Premier League Team",
        "Manchester United": "English Premier League Team",
        "Manchester City": "English Premier League Team",
        "Real Madrid": "Spanish La Liga Team",
        "Barcelona": "Spanish La Liga Team",
        "Roma": "Italian Serie A Team",
        "Bayern Munich": "German Bundesliga Team",
        "Los Angeles": "American MLS Team",
    }
    return teams_map.get(team_name.strip(), "Uncategorized Team")


def match_team_country(team_name: str) -> str:
    """Cross-version pattern matcher compatible across Python 3.3 to 3.13."""
    if sys.version_info >= (3, 10):
        return match_team_country_python310(team_name)
    else:
        return match_team_country_legacy(team_name)


def demo_match() -> None:
    """Run structural pattern matching demonstration."""
    sample_teams: List[str] = ["Manchester", "Real Madrid", "Roma", "Bayern Munich", "Los Angeles"]
    print(f"--- Pattern Matching on Python {sys.version_info.major}.{sys.version_info.minor} ---")
    for team in sample_teams:
        country_info = match_team_country(team)
        print(f"Team: '{team:15s}' -> Category: {country_info}")


if __name__ == "__main__":
    demo_match()
