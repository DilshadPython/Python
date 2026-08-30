"""Legacy Programs Script (Refactored).

This module updates the original `programs.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
"""


class Program:
    """Program class tracking software language and version."""

    def __init__(self, language: str = "Python", version: float = 3.13, skill: str = "Advanced") -> None:
        """Initialize Program."""
        self.language: str = language
        self.version: float = version
        self.skill: str = skill

    def upgrade_version(self, new_version: float) -> None:
        """Upgrade program version."""
        print(f"Updated {self.language} version from {self.version} to {new_version}")
        self.version = new_version


if __name__ == "__main__":
    print("=== Legacy Programs (Refactored) ===")
    p = Program("Python", 3.10, "Intermediate")
    p.upgrade_version(3.13)
