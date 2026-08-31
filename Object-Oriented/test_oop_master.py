"""
Master Unit Test Runner for Object-Oriented Module.

Executes all unit tests across 01-Fundamentals, 02-Advanced, and 03-Exercises subdirectories.
"""
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="Object-Oriented", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
