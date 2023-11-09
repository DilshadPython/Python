a = ('England', 'USA', 'France', 'Germany', 'Spain', 24, -10)

print(a)
print(a[3])

print('-' * 50)

for name in a:
    print(name)
print('-' * 50)
print('\n Adding some number to above tuple \n')
print(a + (0, 221.364, 246e5))


print('\n Now when come back to original tuple the number not been added! \n')
print(a)
print(type(a))
