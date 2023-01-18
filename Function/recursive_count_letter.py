

def count_letter(word):
	if len(word) < 1:
		return 0
	else:
		return len(word[0]) + count_letter(word[1:])

city = str(input('Enter a name of the city: '))

print('The lens of thecity you entered are : ', count_letter(city))