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

print('Copy the list: ')
nums.copy()
print(nums)

print('Clear the list: ')
nums.clear()
print(nums)

nums = [74, 91, 53, 2, 70, 36, 5, 55, 31, 54, -1, 8, 0]
print('Length of the list: ')
print(len(nums))

print('Display the list: ')
print(nums)

print('Remove the number 8: ')
nums.remove(8)
print(nums)

print('Append and pop the number 100: ')
nums.append(100)
print(nums)

print('Pop the last number: ')
nums.pop()
print(nums)

print('Insert the number 100 at the index 3: ')
nums.insert(3, 200)
print(nums)
