import search_books  # as search
# or you can say from search_book import find_book

library = ['Data Science', 'Biology', 'Chimiches',
           'Python Tutorials', 'Django projects']

print('\n Import search function for books!')

item = input('\n Enter the book name you search for: ')
x = str(item)

x = search_books.find_book(library, item)
