books = ['Data Science', 'Biology', 'Chimiches', 'Python Programming', 'Django Frameworks', 'Designing']

print(books)

print('\n - Get all books out from the list and display as normal names and sperate by , . \n')

books_str = ', '.join(books)

print(books_str)

print('\n - Return the books to list using split. \n')

old_books = books_str.split(', ')
print(old_books)

