print('\n Search for the books you need: ')


def find_book(in_lib, target):
	''' Find the book you search for '''
	for key, value in enumerate(in_lib):
		if value == target:
			return print(key, ' Yes found')

	return print(-1, ' Sorry not found')

