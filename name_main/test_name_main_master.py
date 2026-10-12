"""
Master Test Suite Runner for __name__ == '__main__' Tutorial Module.

Discovers and executes all unit test suites across all subdirectories:
- 01-Fundamentals/test_fundamentals.py
- 02-Advanced-Math-and-Operators/test_advanced_operations.py
- 03-Range-Evolution-and-Performance/test_range_performance.py
"""

import importlib.util
from pathlib import Path
import sys
import unittest


def load_module_from_path(module_name: str, file_path: Path):
    """Load a python module dynamically from file path, pushing folder to sys.path."""
    folder = str(file_path.parent.resolve())
    if folder not in sys.path:
        sys.path.insert(0, folder)

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_master_name_main_test_suite() -> bool:
    """Discover and execute all test files in subdirectories."""
    base_dir = Path(__file__).parent.resolve()
    test_files = [
        base_dir / "01-Fundamentals" / "test_fundamentals.py",
        base_dir / "02-Advanced-Math-and-Operators" / "test_advanced_operations.py",
        base_dir / "03-Range-Evolution-and-Performance" / "test_range_performance.py",
    ]

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for idx, t_path in enumerate(test_files):
        if t_path.exists():
            mod_name = f"test_name_main_sub_mod_{idx}"
            mod = load_module_from_path(mod_name, t_path)
            tests = loader.loadTestsFromModule(mod)
            suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_master_name_main_test_suite()
    sys.exit(0 if success else 1)
