# =========================================================================
# SUBFOLDER 02: v37_to_v310_modern_features -> test_37_to_310.py
# =========================================================================
import unittest
from cloud_app.tutorials.python_versions_tutorials.v37_to_v310_modern_features.version_37_to_310_features import (
    demonstrate_python37_to_310_features,
)


class TestPython37To310Subfolder(unittest.TestCase):
    def test_37_to_310_features(self):
        res = demonstrate_python37_to_310_features()
        self.assertEqual(res["3.7_dataclass_name"], "Identity")
        self.assertTrue(res["3.7_dataclass_is_square"])
        self.assertEqual(res["3.7_dict_keys"], ["first", "second", "third"])
        self.assertEqual(res["3.8_pos_only_result"], 25.0)
        self.assertEqual(res["3.8_math_prod"], 120)
        self.assertEqual(res["3.8_walrus_mean"], 40.0)
        self.assertEqual(res["3.8_walrus_filtered"], [55, 70])
        self.assertEqual(res["3.9_dict_union"], {"a": 1, "b": 20, "c": 30})
        self.assertEqual(res["3.9_string_removeprefix"], "NumPy_Array")
        self.assertIn("1D Vector", res["3.10_pattern_1d"])
        self.assertIn("Square 2D Matrix", res["3.10_pattern_square"])
        self.assertIn("Rectangular 2D Matrix", res["3.10_pattern_rect"])
        self.assertEqual(res["3.10_zip_strict"], [(1, "a"), (2, "b"), (3, "c")])


if __name__ == "__main__":
    unittest.main()
