# =========================================================================
# SUBFOLDER 01: v33_to_v36_foundations -> test_33_to_36.py
# =========================================================================
import unittest
import numpy as np

from cloud_app.tutorials.python_versions_tutorials.v33_to_v36_foundations.version_33_to_36_features import (
    demonstrate_python33_to_36_features,
)


class TestPython33To36Subfolder(unittest.TestCase):
    def test_33_to_36_features(self):
        res = demonstrate_python33_to_36_features()
        self.assertEqual(
            res["3.3_yield_from"], ["Python 3.3", "Generator Delegation", "Completed"]
        )
        self.assertEqual(res["3.3_range_slice"], [100, 110, 120, 130])
        self.assertEqual(res["3.4_enum_value"], "active")
        self.assertEqual(res["3.4_pathlib_name"], "demo_file.txt")
        self.assertEqual(res["3.4_statistics_mean"], 30.0)
        self.assertEqual(res["3.5_matmul_result"], [[19.0, 22.0], [43.0, 50.0]])
        self.assertEqual(res["3.6_numeric_literal"], 1_000_000)
        self.assertIn("1,000,000", res["3.6_fstring"])
        self.assertEqual(res["3.6_secure_hex_len"], 8)


if __name__ == "__main__":
    unittest.main()
