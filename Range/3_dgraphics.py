# end is a func for print which is tell end of the print and it will be like that end=''
for x in range(0, 11):
	for y in range(0, 11 - x):
		print(' ', end='')
	print('#')

print('\n========================')

for x in range(0, 11):
	for y in range(0, 11 - x):
		print(' ', end='')
	for a in range(0, x + 1):
		print('0', end='')
	print('')

print('\n========================')

for x in range(0, 11):
	for y in range(0, 11 - x):
		print(' ', end='')
	for a in range(0, 2 *  x + 1):
		print('0', end='')
	print('')