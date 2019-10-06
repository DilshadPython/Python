num = 10
num <<= 2  # multiply by 4 using shift

print(num)
num = 1
for _ in range(5):
    num <<= 1  # *= 2
    print(num)

print('==========================')
num1 = 15
num1 <<= 3  # multiply by 9 using shift

print(num1)
num1 = 2
for _ in range(5):
    num1 <<= 2  # *= 3
    print(num1)
