a = (11, 25, 1, 67, -9, 99, 654, 35, 7, 8, 56)


def minmax(numbers):
    return min(numbers), max(numbers)

print('Using min and max method to display lowerst and heighest number from the tuple')
print(minmax(a))

lower, upper = minmax(a)

print('\n', '#' * 50, '\n')

print('Using lower and upper method to display lowerst and heighest number from the tuple')
print('The lowerst number is :', lower)     # return the smallest numbers
print('#######')
print('The heighest number is :', upper)     # return the largerst number


b = [11, 25, 1, 67, -9, 99, 654, -7, 35, 7, 8, 56, 715]

def minmax_inthe_list(numbers):
    return min(numbers), max(numbers)

lower, upper = minmax_inthe_list(b)

print('The lowerst number is :', lower)     # return the smallest numbers
print('#######')
print('The heighest number is :', upper)     # return the largerst number