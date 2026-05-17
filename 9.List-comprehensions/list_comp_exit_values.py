# Allow creating a new list based on existing values of another list

nums = [74, 91, 53, 2, 70, 36, 5, 55, 31, 54]
# return the number that is even
print([x for x in nums if x % 2 == 0])

# return the number that is odd
print([x for x in nums if x % 2 != 0])

nums.sort()
print(nums)

nums.reverse()
print(nums)