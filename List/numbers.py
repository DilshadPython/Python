number = [6, 9, 12, 15, 18, 21, 24, 28]

print(number)

print('--'*15)
print(number[::-1])

print('--'*15)
num = [6, 9, 12, 15, 18, 21, 24, 28, 31, 34, 38]
print(num)
print('\n The minimam number is ', min(num))

print('\n The maximum number is ', max(num))

print('\n The sum of the numberes are ',sum(num))


print('--'*15)
print(num[5])

print('--'*15)
del num[5]
print(num)

print('--'*15)
print(num[5])

print('--'*15)
print(' we add 9 with 38 here: ')
print(num[1] + num[-1])

print('--'*15)
print(' We add 34 with 28 here from right side: ')
print(num[-2] + num[-4])

print('--'*15)
print(num[0:-1])
