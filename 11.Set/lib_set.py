fruites = {'apples', 'oranges', 'cherry', 'bananas'}
print(fruites)

new = {'mango', 'pinapple'}

print('=============\n')
print(new)

print('==============\n')
print('Update the first set')
fruites.update(new)
print(fruites)

print('==============\n')
for fruit in dir(fruites):
    print(fruit)