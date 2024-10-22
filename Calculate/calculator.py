import math

first = float(input("Enter a number: "))
second = float(input("Enter another number: "))

add = pow(first, 2) + pow(second, 2)
print('Total of add is : ', add)
sqr = math.sqrt(add)
print(f'Sid of sqr = {sqr}')

sub = pow(first, 2) - pow(second, 2)
print('The result of sub is: ', sub)

