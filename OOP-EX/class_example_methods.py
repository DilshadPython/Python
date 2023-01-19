# Design of class

class Name:
	# In the class advance definition we don't need to declare the attribute we 
	# move to constructor methods which is mean instantion or instance of a class

	# constructor methods is a function or methods like below
	def __init__(self, fname, lname, address, postcode):
		# self is the current object of the class
		self.fname = fname
		self.lname = lname
		self.address = address
		self.postcode = postcode
	'''
	to-string methods which is identify the attribut
    This method returns the string representation of the object, his method is called
    when print() or str() function is invoked on an object.
	'''
	def __str__(self):
		return self.fname +' '+ self.lname +' '+ self.address +' '+ self.postcode

# here is define the instance object a_name it means self or an object
a_name = Name('Dilshad', 'Abdulla','1 London raod', 'W12 3LL')
b_name = Name('Tom', 'Smith', '12 Line street', 'SL2 4FL')

print(a_name.fname, '\n', a_name.lname, '\n', a_name.address, '\n', a_name.postcode)
print(b_name.fname, '\n', b_name.lname, '\n', b_name.address, '\n', b_name.postcode)

# This way also print all but if we use an int will display an error because this is str
print(a_name)