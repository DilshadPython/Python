# =========================================================================
# SUBFOLDER 03: v311_to_v313_performance_and_jit -> test_311_to_313.py
# =========================================================================
import unittest
from cloud_app.tutorials.python_versions_tutorials.v311_to_v313_performance_and_jit.version_311_to_313_features import (
    demonstrate_python311_to_313_features,
)


class TestPython311To313Subfolder(unittest.TestCase):
    def test_311_to_313_features(self):
        res = demonstrate_python311_to_313_features()
        self.assertEqual(res["3.11_exception_val_error"], "Invalid Matrix Dimension")
        self.assertEqual(res["3.11_exception_type_error"], "Expected Float64 Dtype")
        self.assertEqual(res["3.11_toml_version"], "3.11")
        self.assertTrue(res["3.11_toml_simd"])
        self.assertIn("Matrix trace is 50", res["3.12_nested_fstring"])
        self.assertTrue(res["3.13_cpython_version"].startswith("3."))
        self.assertTrue(res["unchanged_invariants"]["int_immutability"])
        self.assertTrue(res["unchanged_invariants"]["string_immutability"])


if __name__ == "__main__":
    unittest.main()
