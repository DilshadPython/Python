''' 
regular method and class method will taken the instance as first argument which 
is self in the car_detail or payment method in this example
'''

# clas variables
class Car:

	profit = 1.09
	number_in_the_strore = 0

	def __init__(self, name, model, color, types, price):
		self.name = name
		self.model = model
		self.color = color
		self.types = types 
		self.price = price


		Car.number_in_the_strore += 1


	def car_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.model, self.color, self.types, self.price)


	def payment(self):
		self.price = float(self.price * self.profit)

	'''
	create class method
	'''
	@classmethod
	def set_payment(cls, value):
		cls.profit = value


obj_audi = Car('Audi', 2017, 'Black', 'S3', 33.000)
obj_bmw = Car('BMW', 2016, 'Gray', 'Z3', 28.500)

print('Default profit: ')
print(Car.profit)
print(obj_audi.profit)
print(obj_bmw.profit)

# We try to change the profit now
Car.set_payment(1.17)
print('Change or overwritten profit')
print(Car.profit)
print(obj_audi.profit)
print(obj_bmw.profit)

'''
 We try to change the profit now but use the instance object of audi insted 
 of the Car class see if it works for bmw
'''
obj_audi.set_payment(1.042)
print('Change or overwritten profit using instance object')
print(Car.profit)
print(obj_audi.profit)
print(obj_bmw.profit)