'''
The important point here is we have initializated num in init to 0 and not
defined in the init method after self, in this case you can't add the number
to the obj = Number() because it display an error two arguments is given where
we define only self argument in init method.
'''
class Number(object):
	def __init__(self):
		print('Call __init__ automatically from instance obj')
		self.num = 0


	def increament(self):
		self.num = self.num + 1 


obj = Number()
obj.increament()
obj.increament()

print(obj.num)