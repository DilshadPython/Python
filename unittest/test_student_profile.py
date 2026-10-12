"""
Unit test suite verifying Student class methods, property getters, loan calculations,
and lifecycle fixtures (setUp, tearDown, setUpClass, tearDownClass).
"""
# "import module" loads unittest standard library framework.
import unittest
# "from module import name" imports Student class directly into test scope.
from student_profile import Student


class TestStudentProfile(unittest.TestCase):
    """Test suite covering Student entity initialization, properties, and loan applications."""

    @classmethod
    def setUpClass(cls):
        """Class-level fixture setup executed once before all tests in class."""
        cls.shared_discount = 0.90

    @classmethod
    def tearDownClass(cls):
        """Class-level fixture teardown executed once after all tests in class."""
        pass

    def setUp(self):
        """Per-test fixture setup executed immediately before each test method."""
        self.std_a = Student("Tom", "David", 12370.0)
        self.std_b = Student("Claudia", "Ericson", 14760.0)

    def tearDown(self):
        """Per-test fixture teardown executed immediately after each test method."""
        pass

    def test_email_property(self):
        """Test dynamic student email construction."""
        self.assertEqual(self.std_a.email, "tom.david@university.edu")
        self.assertEqual(self.std_b.email, "claudia.ericson@university.edu")

        # Update student names and verify property recalculation
        self.std_a.first_name = "Elena"
        self.std_a.last_name = "Alan"
        self.assertEqual(self.std_a.email, "elena.alan@university.edu")

    def test_full_name_property(self):
        """Test full name property rendering."""
        self.assertEqual(self.std_a.full_name, "Tom David")
        self.assertEqual(self.std_b.full_name, "Claudia Ericson")

    def test_apply_loan_discount(self):
        """Test loan discount application to tuition balance."""
        self.assertEqual(self.std_a.apply_loan_discount(), 11504.10)
        self.assertEqual(self.std_b.apply_loan_discount(self.shared_discount), 13284.0)

    def test_invalid_initialization(self):
        """Verify initialization raises ValueError for empty names or negative balances."""
        with self.assertRaises(ValueError):
            Student("", "David", 1000.0)
        with self.assertRaises(ValueError):
            Student("Tom", "David", -500.0)


if __name__ == '__main__':
    unittest.main()
