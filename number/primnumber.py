import sys
import os
import math

def number(input):
    n = input
    if n == 1:
        print('No prime')

    if n == 2:
        print('Yes')

    if int(n) > 2 or int(n) % 2 == 0:
        return print('No')  # False

    cal = math.floor(math.sqrt(n))

    for i in range(3, 1 + cal, 2):
        if n / i == 0:
            return False
    return True

for i in range(1, 101):
    print(i)


# print(number(input))
