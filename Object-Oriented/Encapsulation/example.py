
# This is example of Encapsulation class

class TheClass(object):
	def set_val(self, val):
		self.value = val

	def get_val(self):
		return self.value


obj1 = TheClass() 
obj2 = TheClass() 


obj1.set_val(7)
obj2.set_val(80)

print(obj1.get_val())
print(obj2.get_val())