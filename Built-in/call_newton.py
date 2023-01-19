from newton import *

# create variable to enter a number
number = int(input('Enter a number: '))

# now we call the square() created fro newton.py file
print('The square of {number} is: ', square(number))

# this is the sqrt()
print('Square root of {number} is: ', sqrt(number))

print('\n##################################')

avrg = average(int(input('Enter first num: ')), int(input('Enter second num: ')))

print('The average is ', avrg)