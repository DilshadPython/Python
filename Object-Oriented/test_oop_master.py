"""
Master Unit Test Runner for Object-Oriented Module.

Executes all unit tests across 01-Fundamentals, 02-Advanced, and 03-Exercises subdirectories.
"""
# "import module" loads unittest framework and sys path utilities.
import sys
import unittest
from pathlib import Path

# Add subdirectories to sys.path for local module resolution
BASE_DIR = Path(__file__).resolve().parent
for subdir in ["01-Fundamentals", "02-Advanced", "03-Exercises"]:
    subpath = str(BASE_DIR / subdir)
    if subpath not in sys.path:
        sys.path.insert(0, subpath)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for subdir in ["01-Fundamentals", "02-Advanced", "03-Exercises"]:
        discovered = loader.discover(start_dir=str(BASE_DIR / subdir), pattern="test_*.py")
        suite.addTests(discovered)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())
