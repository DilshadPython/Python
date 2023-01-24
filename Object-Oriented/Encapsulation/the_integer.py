# self is an instance of TheIntegeror self is instance of which methods will be called
# Encapsulation class

class TheInteger(object):
	def sent_number(self, num):
		try:
			num = int(num)
		except ValueError:
			return
		self.num = num


	def get_number(self):
		return self.num


	def increment_num(self):
		self.num = self.num + 1

obj = TheInteger()

# we set only int
obj.sent_number(19)
print(obj.get_number())

# try another value but not int
obj.sent_number('Welcome')
print(obj.get_number())

# try another value but float this time
obj.sent_number(88.06)
print(obj.get_number(), '<< Return int not float!')

# We try another instance obj
new_obj = TheInteger()
new_obj.num = 22
print(new_obj.increment_num())

# we try string here we get an error can't concatenate str to int
# new_obj.num = 'Python'
# print(new_obj.increment_num())

try:
	new_obj.num = 'Python3'
	print(new_obj.increment_num())
except:
	print('Error the number is str not int : ', new_obj.num)
