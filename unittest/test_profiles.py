import unittest

from profiles import Student


class TestStudent(unittest.TestCase):

    def test_mail(self):
        std_a = Student('Tom', 'David', 12370)
        std_b = Student('Claudia', 'Ericson', 14760)

        self.assertEqual(std_a.mail, 'Tom.David@gmail.net')
        self.assertEqual(std_b.mail, 'Claudia.Ericson@gmail.net')

        # adding new gmail account
        std_a.firstname = 'Elena'
        std_a.lastname = 'Alan'
        std_b.firstname = 'Anton'
        std_b.lastname = 'George'

        self.assertEqual(std_a.mail, 'Elena.Alan@gmail.net')
        self.assertEqual(std_b.mail, 'Anton.George@gmail.net')

    def test_student_profile(self):
        std_a = Student('Tom', 'David', 12370)
        std_b = Student('Claudia', 'Ericson', 14760)

        self.assertEqual(std_a.student_profile, 'Tom David')
        self.assertEqual(std_b.student_profile, 'Claudia Ericson')

        # adding new student profile
        std_a.firstname = 'Elena'
        std_a.lastname = 'Alan'
        std_b.firstname = 'Anton'
        std_b.lastname = 'George'

        self.assertEqual(std_a.student_profile, 'Elena Alan')
        self.assertEqual(std_b.student_profile, 'Anton George')

    def test_apply_loan(self):
        std_a = Student('Tom', 'David', 12370)
        std_b = Student('Claudia', 'Ericson', 14760)

        std_a.apply_loan()
        std_b.apply_loan()

        # to_pay,
        self.assertEqual(std_a.to_pay, 11504)
        self.assertEqual(std_b.to_pay, 13726)


if __name__ == '__main__':
    unittest.main()
