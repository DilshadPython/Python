books = ['Data Science', 'Biology', 'Chimiches', 'Python Programming', 'Django Frameworks', 'Designing']

print(books.index('Python Programming'))

print('\n - Find the book by boolean. \n')
print('Chimiches' in books)

# or

print('Physics' in books)
print('\n')

for item in books:
	print(item)

print('\n - Display the book with numeric. \n')

for num, item in enumerate(books):
	print(num, item)

print('\n - Display the book with numeric. \n')

for num, item in enumerate(books, start=1):
	print(num, item)