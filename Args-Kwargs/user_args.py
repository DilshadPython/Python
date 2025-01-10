def calculate(*args):
	total = 0

	for arg in args:
		total += arg
	return total


print('Line A: ', calculate(2, 3, 4, 8))
print('Line B: ', calculate(11, 24, 83))
print('Line C: ', calculate(21, 3, 4, 8, 87, 222))
print('Line D: ', calculate(4, 3, 64, 8, 33, 23, -8))

print('\n#############################\n')

def collect(*hello):
	total = 0

	for x in hello:
		total += x
	return total


print('Line E: ',collect(22, 3, -4, 8))
print('Line F: ', collect(141, 24, 83, -99, -34))
print('Line G: ', collect(21, 3, 34, 8, 87, 162))
print('Line H: ', collect(4, 53, 64, 8, 33, 23, -8, -81))