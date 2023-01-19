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
	
	'''
	Notice when we retun self.fname + self.lname will print(b_name) is works
	But if we return self.lname, self.age the print(b_name) doesn't work becs is an int
	'''
	# we can create as much as we want methods in this class
	def fullname(self):
		return self.fname +' '+ self.lname

	def fulladdress(self):
		return self.address, self.postcode

	def initials(self):
		return self.fname[0].upper(), self.lname[0].upper()


	def initials_(self):
		return self.fname[0].upper() + self.lname[0].upper()

# here is define the instance object a_name it means self or an object
b_name = Name('Tom', 'Smith', '12 Line street', 'SL2 4FL')
print(b_name.fname, '\n', b_name.lname, '\n', b_name.address, '\n', b_name.postcode)
print(b_name)

print('\n We call only full name')
print(b_name.fullname())

print('\n We call detail address')
print(b_name.fulladdress())

print(b_name.initials())
print(b_name.initials_())
