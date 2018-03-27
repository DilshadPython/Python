import datetime


class User:
	def __init__(self, fullname, dateofbirth):
		self.mayname = fullname
		self.dateofbirth = dateofbirth # yyyymmdd

		# split or extract fuill name
		split_name = fullname.split(' ')
		self.fname = split_name[0]
		self.lname = split_name[-1]

	def collect_age(self):
		''' Return the number of age '''
		today = datetime.date(2018, 3,28)
		yyyy = int(self.dateofbirth[0:4])
		mm = int(self.dateofbirth[4:6])
		dd = int(self.dateofbirth[6:8])
		dob = datetime.date(yyyy, mm, dd) # the date of birth

		age_in_days = (today - dob).days 
		print(age_in_days)
		age_in_years =  age_in_days / 365
		return int(age_in_years)


user = User('Dilshad Abdulla', '19750301')


print(user.mayname)

print(user.fname)
print(user.lname)

print( user.dateofbirth)
print( user.collect_age())



