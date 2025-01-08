class Doctor:
	def __init__(self, fname, lname, sex, age):
		self.fname = fname
		self.lname = lname
		self.sex = sex
		self.age = age

	def __str__(self):
		return self.fname + self.lname + self.sex + str(self.age)

	def update_name(self, fname, lname):
		self.fname = fname
		self.lname = lname


	def update_age(self):
		self.age = self.age + 1


first_doct = Doctor('James', 'Mark', 'Male', 34)
second_doct = Doctor('Sara', 'Bonar', 'Female', 37)

print('The doctor detals is: ' + str(first_doct))
first_doct.update_name('David', 'Bosh')
first_doct.update_age()
print('The doctor age updated: ' + str(first_doct))
first_doct.update_name('Tomas', 'Alan')
first_doct.update_age()
print('The doctor age updated: ' + str(first_doct))
first_doct.update_name('Russle', 'Bond')
first_doct.update_age()
print('The doctor age updated: ' + str(first_doct))

print( '\n ', second_doct)


