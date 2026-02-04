import random
# start from 5 and end in 74
mynums = list(range(5, 75))
print(mynums)

print()
# now we shuffle the numbers
random.shuffle(mynums)
print(mynums)

print()
nums = random.sample(mynums, 5)
print(nums)

