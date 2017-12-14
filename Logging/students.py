import logging

logging.basicConfig(filename='student.log', level=logging.INFO, 
					format='%(asctime)s:%(levelname)s:%(message)s') 


class Student:

	def __init__(self, std_id, fname, lname, university):
		self.std_id = int(std_id)
		self.fname = fname
		self.lname = lname
		self.university = university 

		logging.info('Create Student: {} - {}, {}, {}. {}'.format(self.std_id, self.fname, 
													self.lname, self.university, 
													self.email))

	@property
	def email(self):
		return '{}-{}@uni.edu'.format(self.fname, self.lname)

	@property
	def name(self):
		return '{}'.format(self.fname, self.lname)

std = Student('0814747', 'Dilshad', 'Abdulla', 'Anglia University')
std_1 = Student('0805321', 'John', 'Kim', 'London University')
std_2 = Student('0866621', 'Rachel', 'Doe', 'London University')
