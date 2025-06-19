"""
class means object that how should look like
An object is created on that class

Example:
    Class Person
    Objects Man, Woman

    cClass Car
    Object Audi, Ferrari
"""
# Create a class
class Car:
    name = 'Audi'

print(Car)

print(Car.name)

print(dir(Car))

print("=======================\n")
print(dir(Car.name))

# Create an object from Car class
my_car = Car()
print('\n================== The object of Car class ==================\n')
print(my_car)
print('=======================================\n')
print(dir(my_car))