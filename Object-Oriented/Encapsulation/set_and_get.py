
# This is example of Encapsulation class

class House:
	# the work process in setter methos is almost like __init__ define the argument
	def set_price(self, price):
		print('\nSETTER METHODS: set_price is set the house price')
		self.price = price
	
	# getter mothos i call the argument define in setter method one argument will be given it is self.
	def get_price(self):
		print('\nGETTER METHODS: get_price is get the price of the house has been set or given.')
		return self.price

obj1 = House() 
obj2 = House() 

obj1.set_price(745662)
obj2.set_price(850434)
print('\nWe can use set the price here as well not in the set_price of SETTER METHODS!')
obj1.price = '444444'
obj2.price = 123123
print(obj2.price)



print(obj1.get_price())
print(obj2.get_price())

print('First house cost: ', obj1.get_price(), '£')
print('Second house cost: ', obj2.get_price(), '£')