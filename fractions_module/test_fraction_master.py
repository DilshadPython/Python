"""
Master Test Suite executing all unit tests across the Fraction tutorial module.
"""
# "import sys" imports system parameters for path resolution.
import sys
# "import unittest" loads standard unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# Add subdirectories to sys.path for direct module discovery.
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "01-Fundamentals"))
sys.path.insert(0, str(BASE_DIR / "02-Advanced-Math-and-Operators"))
sys.path.insert(0, str(BASE_DIR / "03-Range-Evolution-and-Performance"))

# "from test_fundamentals import ..." imports Step 1 test case.
from test_fundamentals import TestFractionFundamentals
# "from test_advanced_math import ..." imports Step 2 test case.
from test_advanced_math import TestFractionAdvancedMath
# "from test_range_evolution import ..." imports Step 3 test case.
from test_range_evolution import TestFractionRangeEvolution


def suite() -> unittest.TestSuite:
    """
    Assemble master test suite combining all 3 step test cases.

    Returns:
        unittest.TestSuite: Combined test suite object.
    """
    loader = unittest.TestLoader()
    master_suite = unittest.TestSuite()
    master_suite.addTest(loader.loadTestsFromTestCase(TestFractionFundamentals))
    master_suite.addTest(loader.loadTestsFromTestCase(TestFractionAdvancedMath))
    master_suite.addTest(loader.loadTestsFromTestCase(TestFractionRangeEvolution))
    return master_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
