# one way to go throw all list
print('A')
for number in [2, 4, 6, 3, 7, 9, 1, 5, 8, 10, 15, 17, 21]:
    print(number, end=' ')

print('\n#################################################')
# another way to go throw the name of list
numbers = [22, 14, 6, 3, 71, 9, 1, 5, 8, 18, 5, 17, 11]

print('\n#################################################')
print('for number in numbers')
for number in numbers:
    print(number, end=' ')

print('\n#################################################')
print('for name in names:')
names = ['Paris', 'London', 'Berlin', 'Tokyo', 'Bruccel', 'Roma']
for name in names:
    print(name, end=' ')

print('\n#################################################')
print('for name in names[2:5]')
for name in names[2:5]:
    print(name, end=' ')

print('\n#################################################')
print('for name in names[:4]')
for name in names[:4]:
    print(name, end=' ')

print('\n#################################################')
print('for name in names[:-5]')
for name in names[:-5]:
    print(name, end=' ')

print('\n#################################################')
print('for name in names[-4:]')
for name in names[-4:]:
    print(name, end=' ')

print('\n#################################################')
print('for name in names[-4:-1]')
for name in names[-4:-1]:
    print(name, end=' ')
