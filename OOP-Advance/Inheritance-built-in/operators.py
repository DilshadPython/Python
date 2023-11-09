name = 'Python'

language = 'English'

details = name + ' ' + language
print(details, ' << using + ')

print('\n', name.__add__(language), ' << __add__()')

print('\n==================================')

num1 = 232
num2 = 137

total = num1 + num2 
print(total, ' using + ')

print(num1.__add__(num2), ' << __add__()')

print(num1.__sub__(num2), ' << __sub__()')

result = num1 - num2
print(result, ' << using - ')
