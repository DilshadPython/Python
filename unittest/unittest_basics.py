"""
cloud_app/tutorials/unittest_basics.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comprehensive, PEP 8 compliant tutorial module demonstrating Python Unittest & Test Automation.

This module provides a structured 3-tier pedagogical architecture for understanding:
1. Core test assertions (assertEqual, assertTrue, assertRaises, assertAlmostEqual, assertIn).
2. Test fixture lifecycles (setUp, tearDown, setUpClass, tearDownClass) and parameterized subtests (self.subTest()).
3. Range sequence protocol verification ($O(1)$ memory, $O(1)$ containment, dir(range)).
4. Reflection matrix (dir(unittest.TestCase)) and CPython 3.13 performance improvements.
5. Cross-version behavioral evolution (Python 2.7 through Python 3.13).
"""

# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import math: Standard library module for mathematical constants (math.pi).
# - import sys: System-specific parameters and functions for memory inspection (sys.getsizeof).
# - import unittest: Python standard library test automation framework.
# - from typing import Any, Dict, List, Optional, Tuple, Union: Type annotations for strict static type checking.
# =========================================================================
import math
import sys
import unittest
from typing import Any, Dict, List, Optional, Tuple, Union

# Define numeric type alias for integers and floats
Numeric = Union[int, float]


# ── 1. Domain Entities & Helper Classes for Testing ───────────────────────────

def add_numbers(a: Numeric, b: Numeric) -> Numeric:
    """Compute the arithmetic sum of two numeric values.

    Args:
        a: First numeric operand.
        b: Second numeric operand.

    Returns:
        Sum of a and b.
    """
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be valid integers or floats.")
    return a + b


def divide_numbers(a: Numeric, b: Numeric) -> float:
    """Compute the quotient of two numeric values.

    Args:
        a: Dividend operand.
        b: Divisor operand.

    Returns:
        Calculated quotient.

    Raises:
        ValueError: If divisor (b) is zero.
        TypeError: If inputs are non-numeric.
    """
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be valid integers or floats.")
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a / b


def calculate_circle_area(radius: Numeric) -> float:
    """Calculate the area of a circle given its radius.

    Args:
        radius: Non-negative numeric radius.

    Returns:
        Calculated circle area (pi * r^2).

    Raises:
        TypeError: If radius is boolean or non-numeric.
        ValueError: If radius is negative.
    """
    if isinstance(radius, bool) or not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a real integer or float number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)


def format_welcome_message(name: str = "Python") -> str:
    """Format a welcome greeting string.

    Args:
        name: Name string to greet.

    Returns:
        Formatted greeting.
    """
    clean_name = str(name).strip() if name else "Guest"
    return f"Welcome back, {clean_name}!"


class StudentProfile:
    """Encapsulates student profile data, email generation, and tuition discount calculations."""

    DEFAULT_LOAN_DISCOUNT: float = 0.93

    def __init__(self, first_name: str, last_name: str, tuition_balance: float) -> None:
        """Initialize StudentProfile instance.

        Args:
            first_name: Student's first name.
            last_name: Student's last name.
            tuition_balance: Tuition balance owed.
        """
        if not first_name.strip() or not last_name.strip():
            raise ValueError("First and last names cannot be empty.")
        if tuition_balance < 0:
            raise ValueError("Tuition balance cannot be negative.")

        self.first_name: str = first_name.strip()
        self.last_name: str = last_name.strip()
        self.tuition_balance: float = float(tuition_balance)

    @property
    def email(self) -> str:
        """Construct student email address dynamically."""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@university.edu"

    @property
    def full_name(self) -> str:
        """Construct student full name dynamically."""
        return f"{self.first_name} {self.last_name}"

    def apply_loan_discount(self, discount_factor: Optional[float] = None) -> float:
        """Apply financial loan discount factor to tuition balance.

        Args:
            discount_factor: Discount multiplier (defaults to DEFAULT_LOAN_DISCOUNT).

        Returns:
            Updated tuition balance.
        """
        factor = discount_factor if discount_factor is not None else self.DEFAULT_LOAN_DISCOUNT
        if factor <= 0:
            raise ValueError("Discount factor must be positive.")
        self.tuition_balance = round(self.tuition_balance * factor, 2)
        return self.tuition_balance


# ── 2. Exemplary Unittest TestCases ──────────────────────────────────────────

class BasicAssertionsTestCase(unittest.TestCase):
    """Demonstrates standard unittest assertion methods."""

    def test_addition_and_division(self) -> None:
        """Verify addition and quotient calculations."""
        self.assertEqual(add_numbers(10, 20), 30)
        self.assertEqual(divide_numbers(100, 4), 25.0)

    def test_exception_handling(self) -> None:
        """Verify defensive exception raising using assertRaises context manager."""
        with self.assertRaises(ValueError) as ctx:
            divide_numbers(10, 0)
        self.assertIn("cannot be zero", str(ctx.exception))

    def test_circle_area_precision(self) -> None:
        """Verify floating point tolerance using assertAlmostEqual."""
        area = calculate_circle_area(5.0)
        self.assertAlmostEqual(area, 78.5398163, places=5)


class StudentFixtureTestCase(unittest.TestCase):
    """Demonstrates test fixture lifecycle hooks (setUp / tearDown) and subtests."""

    def setUp(self) -> None:
        """Runs BEFORE EACH test method to instantiate fresh state."""
        self.student = StudentProfile("Ada", "Lovelace", 1000.0)

    def tearDown(self) -> None:
        """Runs AFTER EACH test method to clean up resources."""
        self.student = None

    def test_student_properties(self) -> None:
        """Verify student full name and dynamic email property."""
        self.assertEqual(self.student.full_name, "Ada Lovelace")
        self.assertEqual(self.student.email, "ada.lovelace@university.edu")

    def test_discount_subtests(self) -> None:
        """Verify parameterized loan discounts using self.subTest()."""
        factors_and_expected = [
            (0.90, 900.0),
            (0.50, 500.0),
            (0.93, 930.0),
        ]
        for factor, expected in factors_and_expected:
            with self.subTest(factor=factor, expected=expected):
                s = StudentProfile("Test", "User", 1000.0)
                self.assertEqual(s.apply_loan_discount(factor), expected)


class AdvancedTestCaseAttributesDemo(unittest.TestCase):
    """Demonstrates TestCase instance attributes, cleanup callbacks, and skipping methods."""

    def setUp(self) -> None:
        """SetUp registering a cleanup callback via self.addCleanup()."""
        self.temp_resource = "active_connection"
        self.addCleanup(self._cleanup_resource)

    def _cleanup_resource(self) -> None:
        """Cleanup function called automatically after tearDown()."""
        self.temp_resource = "closed"

    def test_attributes_and_cleanup(self) -> None:
        """Verify test id(), shortDescription(), maxDiff, and cleanup registration."""
        self.assertEqual(self.temp_resource, "active_connection")
        # Instance reflection attributes & methods
        self.assertTrue(self.id().endswith("test_attributes_and_cleanup"))
        self.assertEqual(self.shortDescription(), "Verify test id(), shortDescription(), maxDiff, and cleanup registration.")
        self.assertTrue(self.longMessage)
        self.assertTrue(isinstance(self.maxDiff, int) or self.maxDiff is None)


# ── 3. Range Sequence Protocol & Reflection Matrix ────────────────────────────

def inspect_range_properties(r: range) -> Dict[str, Any]:
    """Inspect range object sequence properties and O(1) containment.

    Args:
        r: Range object to analyze.

    Returns:
        Structured breakdown of range attributes and dir(range) methods.
    """
    if not isinstance(r, range):
        raise TypeError("Input must be a range object.")

    dir_attrs = dir(r)
    return {
        "start": r.start,
        "stop": r.stop,
        "step": r.step,
        "length": len(r),
        "memory_bytes": sys.getsizeof(r),
        "first_element": r[0] if len(r) > 0 else None,
        "last_element": r[-1] if len(r) > 0 else None,
        "contains_start": r.start in r if len(r) > 0 else False,
        "dir_attributes": [a for a in dir_attrs if not a.startswith("__")],
        "dunder_methods": [a for a in dir_attrs if a.startswith("__")],
    }


def inspect_unittest_attributes_and_methods() -> Dict[str, Any]:
    """Inspect and categorize all attributes and methods across TestCase, TestResult, and TestSuite.

    Returns:
        Structured dictionary categorizing assertion methods, fixture lifecycles,
        testcase instance properties, testresult attributes, and suite tools.
    """
    tc_attrs = dir(unittest.TestCase)
    assertions = sorted([a for a in tc_attrs if a.startswith("assert")])
    fixtures = [a for a in tc_attrs if "setUp" in a or "tearDown" in a or "Cleanup" in a]
    properties = ["id", "shortDescription", "failureException", "longMessage", "maxDiff", "_testMethodName"]

    tr_attrs = dir(unittest.TestResult)
    result_attrs = ["testsRun", "wasSuccessful", "failures", "errors", "skipped", "shouldStop", "addSuccess", "addFailure", "addError"]
    valid_result_attrs = [a for a in result_attrs if hasattr(unittest.TestResult, a) or a in tr_attrs]

    suite_attrs = ["addTest", "addTests", "countTestCases", "run"]
    valid_suite_attrs = [a for a in suite_attrs if hasattr(unittest.TestSuite, a)]

    return {
        "total_testcase_attributes": len(tc_attrs),
        "assertion_methods_count": len(assertions),
        "assertion_methods": assertions,
        "fixture_and_cleanup_methods": fixtures,
        "testcase_instance_properties": properties,
        "testresult_attributes": valid_result_attrs,
        "testsuite_methods": valid_suite_attrs,
        "has_subtest": "subTest" in tc_attrs,
    }


def inspect_testcase_reflection() -> Dict[str, Any]:
    """Inspect unittest.TestCase reflection matrix using dir().

    Returns:
        Categorized dictionary of TestCase assertion methods and lifecycle hooks.
    """
    return inspect_unittest_attributes_and_methods()


# ── 4. Studio Sub-Pane Demonstrations ─────────────────────────────────────────

def demonstrate_basic_unittest_assertions() -> Dict[str, Any]:
    """Run basic arithmetic, string, and circle area test demonstrations."""
    area_res = calculate_circle_area(3.0)
    student = StudentProfile("Guido", "van Rossum", 1500.0)
    discounted = student.apply_loan_discount(0.90)

    return {
        "add_numbers(15, 25)": add_numbers(15, 25),
        "divide_numbers(100, 8)": divide_numbers(100, 8),
        "calculate_circle_area(3.0)": round(area_res, 4),
        "format_welcome_message('Guido')": format_welcome_message("Guido"),
        "student_email": student.email,
        "student_full_name": student.full_name,
        "tuition_after_10_percent_discount": discounted,
    }


def demonstrate_fixtures_and_subtests() -> Dict[str, Any]:
    """Run test suite runner demonstration simulating TestCase execution."""
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicAssertionsTestCase)
    runner = unittest.TextTestRunner(verbosity=0, stream=open("/dev/null", "w"))
    result = runner.run(suite)

    return {
        "tests_run": result.testsRun,
        "was_successful": result.wasSuccessful(),
        "errors": len(result.errors),
        "failures": len(result.failures),
        "skipped": len(result.skipped),
    }


def demonstrate_range_integration() -> Dict[str, Any]:
    """Run range sequence protocol and memory footprint analysis."""
    large_range = range(0, 10_000_000, 5)
    info = inspect_range_properties(large_range)
    return {
        "range_representation": repr(large_range),
        "start": info["start"],
        "stop": info["stop"],
        "step": info["step"],
        "length": info["length"],
        "memory_bytes": info["memory_bytes"],
        "is_constant_memory": info["memory_bytes"] < 100,
        "containment_check_5000": 5000 in large_range,
        "containment_check_5003": 5003 in large_range,
    }


def demonstrate_reflection_matrix() -> Dict[str, Any]:
    """Run TestCase introspection matrix using dir(unittest.TestCase)."""
    return inspect_testcase_reflection()


if __name__ == "__main__":
    print("=== Python Unittest Tutorial Module ===")
    print("Basic Assertions:", demonstrate_basic_unittest_assertions())
    print("Test Runner Result:", demonstrate_fixtures_and_subtests())
    print("Range Integration:", demonstrate_range_integration())
    print("TestCase Reflection:", demonstrate_reflection_matrix())
