animals = ['cat', 'dog', 'walf']

# we display the list of animales
for name in animals:
    print(name)

print('########')
# we print the first name in the animals list
print(animals[1])

name_1 = 'Lion'
name_2 = 'tiger'
name_3 = 'elephant'

# we add the new name to the list
animals.append(name_1)
print(animals)

print('')
animals.append(name_2)
print(animals)

print('')
animals.append(name_3)
print(animals)

print('======================')
for name in animals:
    print(name, end=' ')

print('\n We remove tiger in the list')
animals.remove(name_2)
print(animals)

print('')
animals.append('No animals')
print(animals)

# animals.remove(2)
# print(animals)
