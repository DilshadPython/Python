# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and memory measurement (sys.getsizeof).
# - import math: Standard library module for mathematical functions (math.gcd, math.lcm, math.floor, math.ceil).
# - from decimal import Decimal: Fixed-point and floating-point arithmetic with user-defined precision.
# - from fractions import Fraction: Immutable representation of rational numbers with exact integer numerators and denominators.
# - from typing import Any, Dict, List, Tuple, Union: Type hints for PEP 484 compliance.
# =========================================================================
import math
import sys
from decimal import Decimal
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union


# ─── SUBFOLDER 1: 01-FUNDAMENTALS ─────────────────────────────────────────────


def demonstrate_01_fundamentals_basics(
    numerator: int = 6,
    denominator: int = 8,
    str_val: str = "3/4",
    float_val: float = 0.5,
    dec_val: Decimal = Decimal("0.125"),
) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> fraction_basics.py]
    Demonstrates fundamental Fraction instantiation from integers, strings, floats, and Decimals,
    auto-reduction to lowest terms, and attribute inspection (numerator, denominator).

    Args:
        numerator (int): Numerator integer.
        denominator (int): Denominator integer.
        str_val (str): String representation.
        float_val (float): Floating-point number.
        dec_val (Decimal): Decimal object.

    Returns:
        Dict[str, Any]: Instantiated fractions and properties.
    """
    if denominator == 0:
        raise ZeroDivisionError("Fraction denominator cannot be zero")

    f_int = Fraction(numerator, denominator)  # Auto-simplifies 6/8 -> 3/4
    f_str = Fraction(str_val)
    f_float = Fraction(float_val)
    f_dec = Fraction(dec_val)

    return {
        "f_int_repr": repr(f_int),
        "f_int_str": str(f_int),
        "numerator": f_int.numerator,
        "denominator": f_int.denominator,
        "f_str": str(f_str),
        "f_float": str(f_float),
        "f_dec": str(f_dec),
    }


def demonstrate_01_fundamentals_conversions(
    float_approx: float = math.pi, max_den: int = 10
) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> fraction_conversions.py]
    Demonstrates conversion utilities: limit_denominator(), as_integer_ratio(), is_integer(),
    and standard mathematical GCD / LCM interactions.

    Args:
        float_approx (float): Float to approximate rationally.
        max_den (int): Maximum denominator bound for limit_denominator().

    Returns:
        Dict[str, Any]: Rational approximations and conversion results.
    """
    f_pi = Fraction(float_approx)
    f_limit = f_pi.limit_denominator(max_den)
    f_ratio = Fraction(3, 4)

    return {
        "original_pi_fraction": str(f_pi),
        "limited_pi_fraction": str(f_limit),
        "limited_numerator": f_limit.numerator,
        "limited_denominator": f_limit.denominator,
        "as_integer_ratio": f_ratio.as_integer_ratio(),
        "is_integer_check": Fraction(4, 2).is_integer()
        if hasattr(Fraction, "is_integer")
        else (Fraction(4, 2).denominator == 1),
        "math_gcd": math.gcd(24, 36),
        "math_lcm": math.lcm(12, 18)
        if hasattr(math, "lcm")
        else (12 * 18 // math.gcd(12, 18)),
    }


# ─── SUBFOLDER 2: 02-ADVANCED-MATH-AND-OPERATORS ──────────────────────────────


def demonstrate_02_advanced_arithmetic_ops(
    f1: Fraction = Fraction(3, 4), f2: Fraction = Fraction(1, 2)
) -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> fraction_arithmetic_ops.py]
    Executes advanced arithmetic (+, -, *, /, //, %, **) and relational comparisons
    (==, !=, <, >, <=, >=) between fractions and mixed integer types.

    Args:
        f1 (Fraction): First fraction.
        f2 (Fraction): Second fraction.

    Returns:
        Dict[str, Any]: Map of operational results and comparison booleans.
    """
    if f2 == 0:
        raise ZeroDivisionError("Cannot divide by zero fraction")

    return {
        "addition": str(f1 + f2),
        "subtraction": str(f1 - f2),
        "multiplication": str(f1 * f2),
        "true_division": str(f1 / f2),
        "floor_division": str(f1 // f2),
        "modulus": str(f1 % f2),
        "exponentiation": str(f1**2),
        "is_equal": f1 == Fraction(6, 8),
        "is_greater": f1 > f2,
        "mixed_int_add": str(f1 + 2),  # 3/4 + 2 = 11/4
    }


def demonstrate_02_advanced_math_utilities(
    frac_list: Optional[List[Fraction]] = None,
) -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> fraction_advanced_math.py]
    Applies Python math utilities (math.floor, math.ceil, round, abs) and sum() accumulation
    over lists of fractions with exact Decimal interoperability.

    Args:
        frac_list (List[Fraction]): List of fractions to sum and transform.

    Returns:
        Dict[str, Any]: Advanced math results.
    """
    if frac_list is None:
        frac_list = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)]

    total_sum = sum(frac_list, Fraction(0, 1))
    negative_frac = Fraction(-7, 3)

    return {
        "list_sum": str(total_sum),
        "abs_value": str(abs(negative_frac)),
        "math_floor": math.floor(negative_frac),  # math.floor(-7/3) == -3
        "math_ceil": math.ceil(negative_frac),  # math.ceil(-7/3) == -2
        "round_value": float(round(Fraction(7, 3), 2)),  # 2.33
        "round_fraction": str(round(Fraction(7, 3), 2)),  # "233/100"
        "decimal_interop": str(Fraction(Decimal("0.25")) + total_sum),
    }


# ─── SUBFOLDER 3: 03-RANGE-EVOLUTION-AND-PERFORMANCE ──────────────────────────


def demonstrate_03_range_evolution_and_performance() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Range-Evolution-and-Performance -> fraction_range_evolution.py]
    Demonstrates fractional range generation, memory footprint benchmarks (sys.getsizeof),
    dir(Fraction) introspection matrix, and CPython version evolution (Python 2.7 to 3.13).

    Returns:
        Dict[str, Any]: Range evolution data and performance benchmarks.
    """
    # Create fractional range sequence using step
    fractional_range = [Fraction(i, 4) for i in range(0, 5)]  # [0, 1/4, 1/2, 3/4, 1]

    # Memory benchmarking: materialized list vs range sequence generator
    range_memory = sys.getsizeof(range(0, 1000000))
    list_memory = sys.getsizeof([Fraction(i, 4) for i in range(0, 1000)])

    # Inspection matrix of Fraction methods via dir()
    f_sample = Fraction(3, 4)
    public_attrs = [attr for attr in dir(f_sample) if not attr.startswith("_")]
    dunder_methods = [
        attr
        for attr in dir(f_sample)
        if attr in ("__add__", "__sub__", "__mul__", "__truediv__", "__eq__", "__abs__")
    ]

    return {
        "fractional_range_sequence": [str(x) for x in fractional_range],
        "range_memory_bytes": range_memory,
        "list_memory_bytes": list_memory,
        "public_methods": sorted(public_attrs),
        "dunder_methods": sorted(dunder_methods),
        "cpython_evolution": {
            "python_2_7": "fractions.gcd() resided in fractions module; integer division (1/2) defaulted to floor division (0).",
            "python_3_3": "True float division default; enhanced Fraction string and Decimal constructors.",
            "python_3_9": "fractions.gcd() removed; math.gcd() expanded to arbitrary arguments; Fraction.as_integer_ratio() added.",
            "python_3_13": "CPython optimized C-struct Fraction initialization, free-threaded execution, and sys.set_int_max_str_digits limits.",
        },
    }


def run_all_fractions_module_demos() -> Dict[str, Any]:
    """
    Executes all three subfolder module demonstrations in sequence.
    """
    return {
        "01_fundamentals": {
            "basics": demonstrate_01_fundamentals_basics(),
            "conversions": demonstrate_01_fundamentals_conversions(),
        },
        "02_advanced_math": {
            "arithmetic": demonstrate_02_advanced_arithmetic_ops(),
            "math_utilities": demonstrate_02_advanced_math_utilities(),
        },
        "03_range_and_performance": demonstrate_03_range_evolution_and_performance(),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(run_all_fractions_module_demos())
