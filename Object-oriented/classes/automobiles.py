# clas variables
class Car:

	profit = 1.09
	number_in_the_store = 0

	def __init__(self, name, model, color, types, price):
		self.name = name
		self.model = model
		self.color = color
		self.types = types 
		self.price = price


		Car.number_in_the_store += 1


	def car_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.model, self.color, self.types, self.price)


	def payment(self):
		self.price = float(self.price * self.profit)

instance_audi = Car('Audi', 2017, 'Black', 'S3', 33.000)
instance_bmw = Car('BMW', 2016, 'Gray', 'Z3', 28.500)

print('Audi price before: ', instance_bmw.price)
instance_audi.payment()
print('Audi price with profit: ', instance_audi.price)

print('\n########################################################')

print('BMW price before: ', instance_bmw.price)
instance_bmw.payment()
print('BMW price with profit: ', instance_bmw.price)

print('\n########################################################')
print('The idea here is you can\'t see the profit when you use the instance object')
print(instance_audi.__dict__)
print('\n========================================================')
print('The idea here is you can see the profit when you use the class')
print(Car.__dict__)

# overwritten
instance_audi.payment = 1.7
print('\n**********************************************************************')
print(instance_audi.__dict__)

# now we try to find how many car are in the strore?
print('We have {} numbers of cars in the strore'.format(Car.number_in_the_strore))

