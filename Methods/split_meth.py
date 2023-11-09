print('Split all words by default (,) and set as a list.')
line = input('Enter something: ')

print(line)
print(line.split())

print('\n########################################\n')

print(line.split('.'))

print('\n########################################\n')
print('Split where this character has been entered and removed.\n')

print(line.split('f'))
