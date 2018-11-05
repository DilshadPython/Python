import random


print(dir(random))
print()
# display 10 random number between [0, 1)

for x in range(10):
    print(random.random())


# generate random number between 3, 7
# 1. call random() in [0, 1)
# 2. scale number (multiply by 4) in [0, 1)
# 3. shift number (add3) in [3, 7)

print()
print(10 * '###')


def my_random():
    # random, scale, shift , return ..
    return 4 * random.random() + 3

for x in range(10):
    print(my_random())
