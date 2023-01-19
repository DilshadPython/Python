# Design of class

class Name:
	# In the class advance definition we don't need to declare the attribute we 
	# move to constructor methods which is mean instantion or instance of a class

	# constructor methods is a function or methods like below
	def __init__(self, fname, lname, age, address, postcode):
		# self is the current object of the class
		self.fname = fname
		self.lname = lname
		self.age = age
		self.address = address
		self.postcode = postcode

# here is define the instance object my_name it means self or an object
my_name = Name('Dilshad', 'Abdulla', 44, '1 London raod', 'W12 3LL')
your_name = Name('Tom', 'Smith', 54, '12 Line street', 'SL2 4FL')
