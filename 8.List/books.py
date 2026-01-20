
library = [
    'Data Science',
    'Biology',
    'Chimiches',
    'Python Tutorials',
    'Django projects'
]

print(library[0])

print('===' * 26)

# print all from beginning to the end
print(library[0:])
print('' * 26)

# reverse all books from the list
print(library[::-1])


print('***' * 26)
# print all from beginning to the end
for b in library:
    print('From left to right: ', b)

print('+++' * 15)
# reverse all books from the list
for b in library.__reversed__():
    print('From right to left: ', b)
