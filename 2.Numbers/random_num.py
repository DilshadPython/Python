import random

#Import the random module, and display a random number from 1 to 12:
print(random.randrange(1, 12))

print('\n=======')
# Here display 4 times random number between 1 to 12
for x in random.sample(range(1, 12), 4):
    print(x)

