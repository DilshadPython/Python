number = [7]

number.append(number.append(9))

print('Add one: ', number)
print('\n')
print('#'*40)

nums = [23, 44]

nums.append(nums.append(0))

print('Add one in list with 2 numbers: ', nums)
print('\n')
print('#'*60)

# You can append one number not more
nums.append(nums.append(nums.append(88)))

print('Add after two times try appending: ', nums)
print('\n')
print('#'*80)

# You can append one number not more
nums.append(nums.append(nums.append(nums.append(99))))

print('Add number after 3 times appending: ', nums)