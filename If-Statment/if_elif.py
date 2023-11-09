
print('Please enter a value: ')
a = int(input())
if a > 60:
    print('\nThe number {} is grater than 60 that is true'.format(a))
elif a < 10 and a > 0:
    print('\nThe number {} Yes a is between 0 and 10'.format(a))
else:
    print('\nThe number {} is not between any of above condition'.format(a))
