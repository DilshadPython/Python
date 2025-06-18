fruites = {'apples', 'oranges', 'cherry', 'bananas'}
print(fruites)

print('=================\n')
fruites.remove('oranges')
print(fruites)

print('=================\n')
fruites.discard('bananas')
print(fruites)

print('=================\n')
fruites.add('pineapple')
print(fruites)

print('=================\n')
# pop() remove always the first item in the set
fruites.pop()
print(fruites)