# Crate  a tuple
# Display it how it will work

# Notice: input is raw_input in python version 2.7.12

# Crate a tuple
print('Create empty tuple store which is empty')
storage = ()

if not storage:
    print('Your storage is empty')

input('\nPlease enter to continue: ')

# add items to storage
storage = ('Arsenal', 'Southampton', 'Man Utd', 'Liverpool',
           'Man City', 55.687, 5, 'Chelsea', -12, 'Tottenham')

print(storage[:])

# display
index = int(input('Enter the number in your storage\n'))

print('In inex', index, 'is', storage[index])

start = int(input('\nEnter start number in index: '))
finish = int(input('\nEnter finish number in index: '))

print('storage[', start, ':', finish, ']')
print(storage[start:finish])
input('\nEnter any key to exit: ')
