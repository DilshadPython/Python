# 🔢 Python Fraction Master Module

Welcome to the definitive master tutorial module for **Python Fractions (`fractions.Fraction`)**. This directory features a **3-step sequential curriculum**—guiding students step-by-step from fundamental rational number instantiation and float limit approximations, to advanced arithmetic, rounding, and range sequence memory benchmarks.

---

## 📁 Repository Directory Architecture

```
Fraction/
├── 01-Fundamentals/
│   ├── fraction_basics.py         # Instantiation (ints, str, float, Decimal), reduction & inspection
│   ├── fraction_conversions.py    # limit_denominator(), as_integer_ratio(), type casting & math.gcd()
│   └── test_fundamentals.py       # 9 Unit tests for fundamental operations & conversions
├── 02-Advanced-Math-and-Operators/
│   ├── fraction_arithmetic_ops.py # Arithmetic (+, -, *, /, //, %, **), comparisons & mixed-type arithmetic
│   ├── fraction_advanced_math.py  # math.floor, math.ceil, sum() accumulation & Decimal interop
│   └── test_advanced_math.py      # 7 Unit tests for arithmetic, comparisons & math utilities
├── 03-Range-Evolution-and-Performance/
│   ├── fraction_range_evolution.py# Fractional ranges, sys.getsizeof memory benchmarks, dir(range) introspection
│   └── test_range_evolution.py    # 5 Unit tests for range evolution & memory efficiency
├── fraction.py                    # Standardized PEP 8 master demonstration entrypoint
├── test_fraction_master.py        # Master unittest suite runner executing all 21 unit tests
├── README.md                      # Pedagogical overview & quickstart instructions
└── docs.md                        # Technical documentation, internal dunder hooks & version matrices
```

---

## 🚀 Quickstart & Execution Guide

### 1. Running the Master Demonstration Entrypoint
```bash
python3 Fraction/fraction.py
```

### 2. Running Individual Curriculum Steps
```bash
# Step 1: Fundamentals
python3 Fraction/01-Fundamentals/fraction_basics.py
python3 Fraction/01-Fundamentals/fraction_conversions.py

# Step 2: Advanced Math & Operators
python3 Fraction/02-Advanced-Math-and-Operators/fraction_arithmetic_ops.py
python3 Fraction/02-Advanced-Math-and-Operators/fraction_advanced_math.py

# Step 3: Range Evolution & Performance
python3 Fraction/03-Range-Evolution-and-Performance/fraction_range_evolution.py
```

### 3. Running Unit Test Suites
```bash
# Run Master Test Suite via unittest
python3 Fraction/test_fraction_master.py

# Run Master Test Suite via pytest
pytest Fraction/
```

---

## 💡 Key Pedagogical Concepts Covered

1. **Exact Rational Arithmetic**: Eliminating binary floating-point representation errors (e.g. `0.1 + 0.2 != 0.3` in floats vs `Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10)`).
2. **Float Approximation (`limit_denominator`)**: Finding clean fractional approximations for irrational or floating-point values with bounded denominators.
3. **Range Memory Benchmarks**: Comparing $O(1)$ memory consumption of `range()` vs materialized lists of fractions.
4. **CPython Version Evolution**: Documenting updates from Python 2.7 (where `fractions.gcd` resided in `fractions`) to Python 3.13 (free-threaded execution and Tier 2 JIT speedups).
