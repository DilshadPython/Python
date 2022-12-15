import unittest

from university import Student


class TestStudent(unittest.TestCase):
	# This option use for very large testing and reduce repeat function

	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	# setup method before the test
	def setup(self):
		print('setUp')
		self.std_1 = Student('Tom', 'David', 12370)
		self.std_2 = Student('Claudia', 'Ericson', 14760)
	
	# tearDown method run after the test
	def tearDown(self):
		print('tearDown\n')

	# End of large test

	def test_mail(self):
		print('test_mail')
		self.assertEqual(self.std_1.mail, 'Tom.David@gmail.net')
		self.assertEqual(self.std_2.mail, 'Claudia.Ericson@gmail.net')
		
		# adding new gmail account
		self.std_1.firstname = 'Elena'
		self.std_2.firstname = 'Anton'

		self.assertEqual(self.std_1.mail, 'Elena.Daivd@gmail.net')
		self.assertEqual(self.std_2.mail, 'Anton.Ericson@gmail.net')


	def test_profile(self):
		print('test_profile')
		self.assertEqual(self.std_1.profile, 'Tom David')
		self.assertEqual(self.std_2.profile, 'Claudia Ericson')
		
		# adding new student profile  
		self.std_1.firstname = 'Elena'
		self.std_2.firstname = 'Anton'

		self.assertEqual(self.std_1.profile, 'Elena David')
		self.assertEqual(self.std_2.profile, 'Anton Ericson')

	def test_apply_loan(self):
		print('test_apply_loan')
		self.std_1.apply_loan()
		self.std_2.apply_loan()

								# to_pay, 
		self.assertEqual(self.std_1.to_pay, 13359)
		self.assertEqual(self.std_2.to_pay, 15940)


if __name__ == '__main__':
	unittest.main()
