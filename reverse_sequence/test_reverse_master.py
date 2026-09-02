"""
Master Test Suite executing all unit tests across the Reverse tutorial module.
"""
# "import sys" imports system parameters for path resolution.
import sys
# "import unittest" loads standard unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# Add subdirectories to sys.path for direct module discovery.
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "01-Sequence-Reversal-Basics"))
sys.path.insert(0, str(BASE_DIR / "02-Advanced-Reversal-Protocols"))
sys.path.insert(0, str(BASE_DIR / "03-Range-Reversal-and-Performance"))

# "from test_reversal_basics import ..." imports Step 1 test case.
from test_reversal_basics import TestReversalBasics
# "from test_reversal_protocols import ..." imports Step 2 test case.
from test_reversal_protocols import TestReversalProtocols
# "from test_range_reversal import ..." imports Step 3 test case.
from test_range_reversal import TestRangeReversal


def suite() -> unittest.TestSuite:
    """
    Assemble master test suite combining all 3 step test cases.

    Returns:
        unittest.TestSuite: Combined test suite object.
    """
    loader = unittest.TestLoader()
    master_suite = unittest.TestSuite()
    master_suite.addTest(loader.loadTestsFromTestCase(TestReversalBasics))
    master_suite.addTest(loader.loadTestsFromTestCase(TestReversalProtocols))
    master_suite.addTest(loader.loadTestsFromTestCase(TestRangeReversal))
    return master_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())
