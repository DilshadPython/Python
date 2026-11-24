"""Loop Control Statements ('break', 'continue') and Nested Loops in Python.

Demonstrates basic 'for' loop iteration, loop interruption using 'break',
skipping loop steps using 'continue', and cartesian product nested loops.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing imports for list and tuple hints.
"""

from typing import List, Tuple


def iterate_names_basic(names: List[str]) -> List[str]:
    """Iterate and print all names in a list."""
    seen: List[str] = []
    for name in names:
        seen.append(name)
        print(name)
    return seen


def demonstrate_break(names: List[str], target: str = "Rob") -> List[str]:
    """Iterate through names and terminate loop execution when target is encountered."""
    processed: List[str] = []
    print(f"\n--- Demonstrating 'break' on target '{target}' ---")
    for name in names:
        if name == target:
            print(f"\n The target name '{target}' was found! Breaking loop.")
            break
        processed.append(name)
        print(name)
    return processed


def demonstrate_continue(names: List[str], target: str = "Rob") -> List[str]:
    """Iterate through names and skip printing when target is encountered."""
    processed: List[str] = []
    print(f"\n--- Demonstrating 'continue' on target '{target}' ---")
    for name in names:
        if name == target:
            print(f"\n - The name '{target}' was found (skipping item)\n")
            continue
        processed.append(name)
        print(name)
    return processed


def demonstrate_nested_loops(
    names: List[str], numbers: List[int]
) -> List[Tuple[str, int]]:
    """Execute a nested loop creating pairs of names and numbers."""
    pairs: List[Tuple[str, int]] = []
    print("\n--- Demonstrating Nested 'for' Loops ---")
    for name in names:
        for num in numbers:
            pairs.append((name, num))
            print(f"{name} {num}")
    return pairs


def demo_for_loop() -> None:
    """Run loop control structures and nested loop demonstration."""
    sample_names = ["Tom", "Chris", "Julia", "Rob", "Claudio", "Sarah", "Amanda"]
    sample_numbers = [1, 2, 3, 4, 5, 6, 7]

    print("=== 1. Basic Loop Iteration ===")
    iterate_names_basic(sample_names)

    print("=== 2. Loop Break Execution ===")
    demonstrate_break(sample_names, "Rob")

    print("=== 3. Loop Continue Execution ===")
    demonstrate_continue(sample_names, "Rob")

    print("=== 4. Nested Loop Product ===")
    demonstrate_nested_loops(sample_names[:3], sample_numbers[:3])


if __name__ == "__main__":
    demo_for_loop()
