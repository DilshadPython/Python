"""
Unit test suite verifying range object sequence properties, O(1) containment testing,
and reflection inspection using dir(range) and dir(unittest.TestCase).
"""
# "import module" loads unittest from standard library.
import unittest


class TestRangeAndReflectionIntegration(unittest.TestCase):
    """Test suite covering range sequence protocol methods and reflection matrix."""

    def test_range_sequence_properties(self):
        """Verify range start, stop, step properties and slicing."""
        r = range(10, 100, 5)
        self.assertEqual(r.start, 10)
        self.assertEqual(r.stop, 100)
        self.assertEqual(r.step, 5)
        self.assertEqual(len(r), 18)
        self.assertEqual(r[0], 10)
        self.assertEqual(r[-1], 95)

    def test_range_constant_time_containment(self):
        """Verify O(1) mathematical containment testing on large range sequence."""
        large_range = range(0, 1_000_000_000, 10)
        self.assertIn(500_000, large_range)
        self.assertNotIn(500_005, large_range)

    def test_range_dir_reflection(self):
        """Verify range object attributes via dir(range)."""
        r = range(5)
        attrs = dir(r)
        self.assertIn('start', attrs)
        self.assertIn('stop', attrs)
        self.assertIn('step', attrs)
        self.assertIn('count', attrs)
        self.assertIn('index', attrs)
        self.assertIn('__contains__', attrs)

    def test_testcase_dir_reflection(self):
        """Verify unittest.TestCase attribute reflection via dir()."""
        test_attrs = dir(self)
        self.assertIn('assertEqual', test_attrs)
        self.assertIn('assertAlmostEqual', test_attrs)
        self.assertIn('assertRaises', test_attrs)
        self.assertIn('setUp', test_attrs)
        self.assertIn('tearDown', test_attrs)


if __name__ == '__main__':
    unittest.main()
