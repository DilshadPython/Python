import random

book_store = ['Data Science', 'Biology', 'Chimiches',
              'Python', 'Django', 'Java', 'CPlusPlus']

print(random.choice(book_store))

print('##############')

for book in random.choice(book_store):
    print(book)
