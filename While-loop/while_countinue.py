# numerator and denumerator which is user decide to enter
numerator = 0
denumerator = 0

# if you print -1 the program will stop
while denumerator != -1:
	print('Enter a numerator: ')
	numerator = float(input())
	print('\nEnter a denumerator: ')
	denumerator = float(input())
	# if the enter the denumerator to 0 the program will go back to begining
	if denumerator == 0:
		continue
	print(numerator / denumerator)