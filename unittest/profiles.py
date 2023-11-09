

class Student:

	pay_raise = 0.93

	# definitions
	def __init__(self, firstname, lastname, to_pay):
		self.firstname = firstname
		self.lastname = lastname
		self.to_pay = to_pay


	@property
	def mail(self):
		return '{}.{}@gmail.net'.format(self.firstname, self.lastname)

	@property
	def student_profile(self):
		return '{} {}'.format(self.firstname, self.lastname)

	def apply_loan(self):
		self.to_pay = int(self.to_pay * self.pay_raise)
