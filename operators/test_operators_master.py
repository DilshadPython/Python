"""
Master Test Suite executing all unit tests across the Operators tutorial module.
"""
# "import module" loads sys and unittest standard library framework.
import sys
import unittest
# "from pathlib import Path" imports Path for workspace directory resolution.
from pathlib import Path

# Add module subdirectories to sys.path for test discovery
CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR / "01-Arithmetic-and-Assignment"))
sys.path.insert(0, str(CURRENT_DIR / "02-Comparison-and-Logical"))
sys.path.insert(0, str(CURRENT_DIR / "03-Advanced-Operators-and-Range"))

# Import test classes from submodules
from test_advanced_range import TestAdvancedOperatorsAndRange
from test_arithmetic_assignment import TestArithmeticAndAssignmentOperators
from test_comparison_logical import TestComparisonAndLogicalOperators


def suite() -> unittest.TestSuite:
    """
    Assemble master test suite combining all 3 step test cases.

    Returns:
        unittest.TestSuite: Combined test suite object.
    """
    loader = unittest.TestLoader()
    master_suite = unittest.TestSuite()
    master_suite.addTest(loader.loadTestsFromTestCase(TestArithmeticAndAssignmentOperators))
    master_suite.addTest(loader.loadTestsFromTestCase(TestComparisonAndLogicalOperators))
    master_suite.addTest(loader.loadTestsFromTestCase(TestAdvancedOperatorsAndRange))
    return master_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
