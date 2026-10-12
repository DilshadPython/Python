"""
01-Arithmetic-and-Assignment/advanced_arithmetic_and_assignment_examples.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advanced Arithmetic & In-Place Assignment Examples:
1. Complex Number Arithmetic Operations
2. Fast Modular Exponentiation & Floor Remainder Edge Cases
3. In-place List & Set Operations using Augmented Operators (+=, *=, &=, |=)
"""
# Standard library typing symbols
from typing import Dict, List, Set, Tuple


def calculate_complex_arithmetic(c1: complex, c2: complex) -> Dict[str, complex]:
    """
    Demonstrate complex number arithmetic (+, -, *, /).

    Args:
        c1 (complex): First complex number.
        c2 (complex): Second complex number.

    Returns:
        Dict[str, complex]: Results of complex arithmetic calculations.
    """
    return {
        "addition": c1 + c2,
        "subtraction": c1 - c2,
        "multiplication": c1 * c2,
        "division": c1 / c2,
    }


def demonstrate_inplace_sequence_mutations() -> Tuple[List[int], Set[int]]:
    """
    Demonstrate augmented assignment operators on mutable sequences (lists, sets).

    Returns:
        Tuple[List[int], Set[int]]: Mutated list and set objects.
    """
    numbers_list = [1, 2, 3]
    numbers_list += [4, 5]     # Equivalent to list.extend([4, 5]) in-place
    numbers_list *= 2          # Replicates elements in-place

    tags_set = {10, 20, 30}
    tags_set |= {40, 50}       # In-place Set Union
    tags_set &= {20, 30, 40}   # In-place Set Intersection

    return numbers_list, tags_set
