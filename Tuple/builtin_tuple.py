name = tuple()

print(dir(name))


# https://www.samsung.com/uk/support/model/LC49RG90SSUXEN/#downloads
nums = (3, 7, 11, 6, 3, 17, 11, 23, 0, 9, 11)

print('Display all numbers : ', nums)
print('\n')

# nums[0] = 2

# print('Try to change number 3 as first number to number 2')
# print(nums)
# output
'''
 nums[0] = 2
TypeError: 'tuple' object does not support item assignment
Tuple is not mutable you can't change
'''
print('We can count how many times a number duplicated using .count(value) >> ', nums.count(11))
print('\n')

print('We can index the place of a number in tuple index[] >> ', nums[2])
print('\n')
