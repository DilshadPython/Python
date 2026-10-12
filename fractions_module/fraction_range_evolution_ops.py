"""Fractional Range Evolution, Sequence Generation, & Introspection Module.

Provides functions demonstrating:
- Fractional range sequence generation
- O(1) space memory footprint comparison between `range()` and `List[Fraction]`
- Introspection of `range` object attributes via `dir(range)`
- Python version evolution breakdown from Python 2.7 to Python 3.13
"""

import sys
from fractions import Fraction
from typing import Any, Dict, List


def generate_fractional_range(
    start: Fraction, stop: Fraction, step: Fraction
) -> List[Fraction]:
    """Generate a list of Fraction values over a fractional start, stop, and step range.

    Since standard `range()` only supports integer arguments, fractional steps are generated
    by iterating with step increments in a loop.

    Args:
        start: Starting fraction value inclusive.
        stop: Stopping fraction bound exclusive.
        step: Step increment fraction.

    Returns:
        List of exact Fraction step values.
    """
    result: List[Fraction] = []
    current = start
    if step > 0:
        while current < stop:
            result.append(current)
            current += step
    elif step < 0:
        while current > stop:
            result.append(current)
            current += step
    return result


def compare_range_and_fraction_memory_efficiency(
    element_count: int = 1000
) -> Dict[str, Any]:
    """Compare O(1) memory footprint of `range()` vs materialized `List[Fraction]`.

    Performance Note:
    - `range()` stores only start, stop, and step attributes in C memory (~48 bytes), operating in O(1) space.
    - Materialized sequence lists store individual object pointers in memory, scaling linearly in O(N) space.

    Args:
        element_count: Number of items in range sequence.

    Returns:
        Memory size comparison in bytes.
    """
    r = range(element_count)
    fraction_list = [Fraction(i, 3) for i in range(element_count)]

    return {
        "element_count": element_count,
        "range_bytes": sys.getsizeof(r),
        "fraction_list_bytes": sys.getsizeof(fraction_list),
        "single_fraction_bytes": sys.getsizeof(Fraction(1, 3)),
        "is_range_constant_memory": sys.getsizeof(range(10)) == sys.getsizeof(range(1_000_000)),
    }


def inspect_range_attributes_and_methods() -> Dict[str, Any]:
    """Demonstrate introspection of range object attributes using `dir(range)`.

    Returns:
        Range attributes matrix and public methods list.
    """
    r = range(10, 100, 5)
    public_attrs = [attr for attr in dir(range) if not attr.startswith("__")]

    return {
        "range_object": str(r),
        "start": r.start,
        "stop": r.stop,
        "step": r.step,
        "public_methods_and_attrs": public_attrs,
        "index_of_25": r.index(25),
        "count_of_25": r.count(25),
        "containment_check_50": 50 in r,
    }


def document_python_version_evolution() -> Dict[str, str]:
    """Summarize version evolution of fractions and range from Python 2.7 to Python 3.13.

    Returns:
        Evolution notes per major Python release milestone.
    """
    return {
        "Python 2.7": (
            "fractions.gcd() lived in fractions module; xrange() generated lazy ranges; "
            "Fraction string parser had strict syntax requirements."
        ),
        "Python 3.0-3.4": (
            "range() replaced xrange() with O(1) memory sequence type; unified int type; "
            "Fraction implemented numbers.Rational abstract base class."
        ),
        "Python 3.5-3.8": (
            "fractions.gcd() moved to math.gcd() in 3.5; Fraction.as_integer_ratio() added in 3.8 "
            "matching float.as_integer_ratio()."
        ),
        "Python 3.9-3.11": (
            "fractions.gcd() removed in 3.9; Fraction constructor supports whitespace in string "
            "expressions like Fraction(' 1 / 3 '); CPython Specializing Adaptive Interpreter (3.11) "
            "accelerates binary fraction arithmetic."
        ),
        "Python 3.12-3.13": (
            "Fraction constructor supports string ints with exponents; CPython 3.13 free-threaded "
            "execution (PEP 703) enables parallel multi-threaded fraction computations."
        ),
    }


def main() -> None:
    """Demonstrate fractional range and memory inspection operations."""
    print("--- Fractional Range & Introspection Operations ---")

    f_range = generate_fractional_range(Fraction(0, 1), Fraction(1, 1), Fraction(1, 4))
    print(f"[generate_fractional_range] [0 to 1 step 1/4]: {f_range}")

    mem_info = compare_range_and_fraction_memory_efficiency(1000)
    print(f"\n[memory_efficiency] {mem_info}")

    range_info = inspect_range_attributes_and_methods()
    print(f"\n[dir(range) introspection] {range_info}")


if __name__ == "__main__":
    main()
