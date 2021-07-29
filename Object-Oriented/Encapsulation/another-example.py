
# Encapsulation class

class TheInteger(object):
	def set_val(self, val):
		try:
			val = int(val)
		except ValueError:
			return
		self.val = val


	def get_val(self):
		return self.val


	def increment_val(self):
		self.val = self.val + 1

obj = TheInteger()

obj.set_val(19)
print(obj.get_val())

# try another value but not int
obj.set_val('Welcome')
print(obj.get_val())

# We try string
obj.val = 'Python'
print(obj.increment_val())