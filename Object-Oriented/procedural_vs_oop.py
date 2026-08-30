"""Procedural vs Object-Oriented Paradigm Demonstration Module.

This module compares procedural programming (global variable mutation and sequential procedures)
against Object-Oriented Programming (encapsulated state inside class instances).
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Dict, Any


def run_procedural_example() -> int:
    """Execute procedural state manipulation using simple sequential arithmetic.

    Returns:
        Final integer value.
    """
    val = 2
    val += 1
    val += 1
    val += 1
    return val


class CustomerCounter:
    """Class representing an encapsulated customer counter (Object-Oriented Paradigm)."""

    def __init__(self, initial_count: int = 0) -> None:
        """Initialize CustomerCounter with an initial count."""
        self._count: int = initial_count

    def increment(self, amount: int = 1) -> None:
        """Increment customer count cleanly via method.

        Args:
            amount: Integer step to add.
        """
        self._count += amount

    @property
    def count(self) -> int:
        """Get current customer count."""
        return self._count


def compare_paradigms() -> Dict[str, Any]:
    """Execute both procedural and object-oriented paradigms and return comparison analysis.

    Returns:
        Dictionary containing results and paradigm explanations.
    """
    proc_result = run_procedural_example()

    counter = CustomerCounter(initial_count=2)
    counter.increment(1)
    counter.increment(1)
    counter.increment(1)
    oop_result = counter.count

    return {
        "procedural": {
            "result": proc_result,
            "description": "Procedural: State stored in loose scalar variables, mutated via direct instructions.",
        },
        "object_oriented": {
            "result": oop_result,
            "description": "Object-Oriented: State encapsulated within CustomerCounter instance, modified via methods.",
        },
    }


if __name__ == "__main__":
    print("=== Procedural vs Object-Oriented Paradigm Comparison ===")
    analysis = compare_paradigms()
    print("1.", analysis["procedural"]["description"])
    print("   Result:", analysis["procedural"]["result"])
    print("\n2.", analysis["object_oriented"]["description"])
    print("   Result:", analysis["object_oriented"]["result"])
