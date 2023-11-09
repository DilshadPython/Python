
class Veichle(object):
	# Here we initionlise the class, self represent an instance of Dog
	def __init__(self, reg, types, gas):
		self.reg = reg
		self.types  = types
		self.gas = gas


	def description(self):
		print(f"My Veichle reg {self.reg}, type {self.types}, the tank is {self.gas} liter.")

	def fill_uptank(self):
		self.gas = 120

	def empty_tank(self):
		self.gas = 0

	def gas_left(self):
		self.gas = gas


# Inheritance

class Car(Veichle):
	# This is constructor method and super() stand for Dog class here.
	# if I define description method here we will overwrite the privouse one
	# in dog class
	def __init__(self, reg, types, gas):
		super().__init__(reg, types, gas)

	def max_speed(self, speed):
		self.speed = speed
		

class Van(Veichle):
	# This is constructor method and super() stand for Dog class here.
	# if I define description method here we will overwrite the privouse one
	# in dog class
	def __init__(self, reg, types, gas, tires):
		super().__init__(reg, types, gas)
		self.tires = tires

	def max_speed(self, speed):
		self.speed = speed
		

mycar = Car('AM80 YTR', 'Audi', 80)
mycar.description()
mycar.max_speed(220)

myvan = Van('RM69 GHT', 'Ford transit', 120, '6 tires')
myvan.description()
myvan.max_speed(120)

