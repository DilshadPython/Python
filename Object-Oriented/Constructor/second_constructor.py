'''
In this example we defined the number in __init__ method we can pass the number
directly in the obj = Number(3), we define two argument self and number
'''
class Number(object):
	def __init__(self, value):
		print('Call __init__ automatically from instance obj')
		self.val = value


	def increament(self):
		self.val = self.val + 1 


obj = Number(3)
print(obj.val)

print('\nIncreaments two time and the result below')
obj.increament()
obj.increament()

print(obj.val)