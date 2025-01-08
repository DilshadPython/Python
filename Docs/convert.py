weight = int(input('Enter weight: '))

unit = input("(Kg) Kilogramme or (G) Gramme ")

if unit.upper() == 'KG':
	converted = weight * 1000
	print(converted)
else:
	convert = weight ** 10
	print(weight + convert)
