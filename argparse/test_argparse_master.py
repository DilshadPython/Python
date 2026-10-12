"""
Master Unit Test Suite Runner for the Argparse Module.

Executes unit test suites across all 3 pedagogical sub-tiers:
1. 01-Fundamentals (basic_argparse tests)
2. 02-Advanced-Parsing-and-Subcommands (advanced_argparse tests)
3. 03-Range-Evolution-and-Performance (range_argparse tests)

PEP 8 compliant, fully automated test runner for Python 2.7 - 3.13 environments.
"""

import sys
from pathlib import Path
import unittest

# Ensure sub-tier directories are included in Python system path for seamless module importing
MODULE_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(MODULE_ROOT / "01-Fundamentals"))
sys.path.insert(0, str(MODULE_ROOT / "02-Advanced-Parsing-and-Subcommands"))
sys.path.insert(0, str(MODULE_ROOT / "03-Range-Evolution-and-Performance"))


def run_all_argparse_tests() -> unittest.TestResult:
    """
    Discovers and executes all unit tests within the argparse module directory.

    Returns:
        unittest.TestResult: Summary of test execution results.
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Discover test files across all sub-tiers
    tier1 = loader.discover(str(MODULE_ROOT / "01-Fundamentals"), pattern="test_*.py")
    tier2 = loader.discover(str(MODULE_ROOT / "02-Advanced-Parsing-and-Subcommands"), pattern="test_*.py")
    tier3 = loader.discover(str(MODULE_ROOT / "03-Range-Evolution-and-Performance"), pattern="test_*.py")

    suite.addTests(tier1)
    suite.addTests(tier2)
    suite.addTests(tier3)

    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    result = run_all_argparse_tests()
    sys.exit(not result.wasSuccessful())
