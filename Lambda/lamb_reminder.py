# lambda is a small function with unknown name

# Please enter a number
num = int(input('Enter a number: '))

# lambda take the num and calculate
result = lambda num: num - 5

# We will display the result and passing the number to the result
print('{} % 8 = {}'.format(num, result(num)))
print(result(num))
