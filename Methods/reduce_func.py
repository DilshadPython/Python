from functools import reduce

# Multiply all nums to the number in the list

data = [2.3, 12, -0.7, 6.7, 3.13, 22.03, 9.11]

result = lambda x, y: x * y

print(reduce(result, data))

print()

num = 1

for i in data:
    num = num * i

print(num)
