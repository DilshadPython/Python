
nums = [4, 5, 7, 5, 4, 8]
total = 0
# for num in nums:
#     total = sum(num)
#     print(total)

total = sum(nums)
print(total)
print('##################\n')

output = set()

for num in nums:
    if num not in nums:
        output = sum(int(num))
        print(output)


