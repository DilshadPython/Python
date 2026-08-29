def vowels_count(var = str(input('Enter a name: '))):
	output = var.lower()
	count = 0
	for x in range(len(var)):
		if var[x] == 'a' or var[x] == 'e' or var[x] == 'i' or var[x] == 'o' \
			or var[x] == 'u' or var[x] == 'q':
			count += 1
	return count 


print('We found ', vowels_count(), ' vowels in the name.')
