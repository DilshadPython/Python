"""
Master Unit Test Suite Runner for the Artificial Intelligence (ai_python) Module.

Executes unit test suites across all 3 pedagogical sub-tiers:
1. 01_fundamentals (mnist_classifier_basics tests)
2. 02_advanced_model_architecture (advanced_neural_network tests)
3. 03_range_evolution_and_performance (range_epoch_performance tests)

PEP 8 compliant, fully automated test runner for Python 2.7 - 3.13 environments.
"""

import sys
from pathlib import Path
import unittest

# Ensure sub-tier directories are included in Python system path
MODULE_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(MODULE_ROOT / "01_fundamentals"))
sys.path.insert(0, str(MODULE_ROOT / "02_advanced_model_architecture"))
sys.path.insert(0, str(MODULE_ROOT / "03_range_evolution_and_performance"))


def run_all_ai_python_tests() -> unittest.TestResult:
    """
    Discovers and executes all unit tests within the ai_python module directory.

    Returns:
        unittest.TestResult: Summary of test execution results.
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Discover test files across all sub-tiers
    tier1 = loader.discover(str(MODULE_ROOT / "01_fundamentals"), pattern="test_*.py")
    tier2 = loader.discover(str(MODULE_ROOT / "02_advanced_model_architecture"), pattern="test_*.py")
    tier3 = loader.discover(str(MODULE_ROOT / "03_range_evolution_and_performance"), pattern="test_*.py")

    suite.addTests(tier1)
    suite.addTests(tier2)
    suite.addTests(tier3)

    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    result = run_all_ai_python_tests()
    sys.exit(not result.wasSuccessful())
