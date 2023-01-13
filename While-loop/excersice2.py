# Create calculater using while loop

var_1 = 0.0
var_2 = 0.0

op = ''

while var_1 != 'q':
	print('Enter your first number or enter q to exit here: ', )
	var_1 = input()
	if var_1 == 'q':
		print('You are exit from the program.')
		break
	var_1 = float(var_1)
	print('Enter your second number :')
	var_2 = float(input())
	print('Enter the operation to calculate [+, -, *. /] ')
	op = input()
	if op == '+':
		print(var_1 + var_2)
	elif op == '-':
		print(var_1 - var_2)
	elif op == '*':
		print(var_1 * var_2)
	elif op == '/':
		print(var_1 / var_2)
	else:
		print('\n You entered not recogize operater!')
