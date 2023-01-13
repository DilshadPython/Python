guese = 0
answer = 'Google'

while guese <= 3:
	print('Please enter the name of the best search browser:')
	respond = input()
	guese = guese + 1
	if respond == 'Google':
		print('Well done that is correct answer :)')
		# to stop the program if the answer is correct you have to write break
		break
	elif guese == 3:
		print('\nSorry, your gueses was wrong the answer was Google')
		break
	else:
		print('\nSorry wrong answer try again.')