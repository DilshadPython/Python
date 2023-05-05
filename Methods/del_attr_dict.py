cars = {
	'name': 'Audi',
	'years': 2005,
	'models': 'A3',
	'name': 'Volvo',
	'years': 2010,
	'models': 'EX90'
}

del_name = str(input('Enter name: '))

delattr(cars, del_name)

del cars.name
print(cars)