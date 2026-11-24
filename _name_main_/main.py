"""Main entry point script demonstrating environment variable inspection.

Shows safe environment variable retrieval using `os.environ` and `os.getenv`.
"""

import os
from typing import Optional


def get_environment_summary(variable_name: str = "USER") -> dict[str, Optional[str]]:
    """Retrieve environment info safely without dumping sensitive system secrets.

    Args:
        variable_name (str): Environment variable key to inspect (default: 'USER').

    Returns:
        dict[str, Optional[str]]: Summary of selected environment variable.
    """
    value = os.getenv(variable_name, "Not Set")
    total_vars = len(os.environ)

    print(f"Author / User identifier: DILSHAD")
    print(f"Inspected Environment Variable '{variable_name}': {value}")
    print(f"Total environment variables registered: {total_vars}")

    return {
        "author": "DILSHAD",
        "variable_inspected": variable_name,
        "value": value,
        "total_variables": str(total_vars),
    }


def main() -> int:
    """Script entry point."""
    get_environment_summary("USER")
    return 0


if __name__ == "__main__":
    main()
