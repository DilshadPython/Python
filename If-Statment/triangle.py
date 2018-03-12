


first = int(input('The length of the side first = '))
second = int(input('The length of the side second = '))
third = int(input('The length of the side third = '))

if first != second and second != third and first != third:
	print('We have Scalene triangle')
elif first == second and second == third:
	print('We have equilateral triangle')
else:
	print('We have isosceles triangle!')