
nums = [4, 5, 7, 5, 4, 8]
total = 0
for num in nums:
    total = num + total
    print(total, ' << This is for loops')

total = sum(nums)
print('\n Totals: ', total, ' << ')
print('\n==================')

output = set()

for num in nums:
    print('\n\t', num, '\t' )
print('******************\n')
# set remove all duplicated number s in the list
x = set(nums)
print('Set remove all duplicates number in the nums list and change the list to set: \n', x, '\n')
