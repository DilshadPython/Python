class Car:
	name = 'Volvo'
	years = 2010
	models = 'EX90'

obj = Car()
print('name: ',obj.name,'\n', 'years: ', obj.years,'\n', 'models: ', obj.models)


print('Testint to see if delete it : \n')

print('Car', Car.__dict__, '\n')
# here we delete the car name 
delattr(Car, 'name')
print('Car after delattr: ', Car.__dict__)

print('\n =============================')
for attr, value in Car.__dict__.items():
	if not attr.startswith('__'):
		print(attr, ' = ', value)
