
# print(help(sorted))
'''
Help on built-in function sorted in module builtins:

sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
(END)
'''

numbers = (8, 5, 3, 1, 6, 7, 10, 2, 10, 4, 9)

print('We will sorted the tuple in line 14 all in one line')
data = sorted(numbers)
print(data)

print()
print('This print return the original number in line 14')
print(numbers)

print()
print('We will sorted the string below start first with empty space than capital character and all\
 lower character but alpabetically.')

print('===='*30)
print(sorted('Manchster United'))