'''
list comprehensions

[expr for val in collection]
[expr for val in collection if <test>]
[expr for val in collection if <test> and <test>]
'''

my_list = []

for x in range(1, 221):
	my_list.append(x**2)


print(my_list)

## list comprehenstion way
print('====================================================')
print('====================================================')
result = [x**2 for x in range(1, 121)]

print(result)

print('====================================================')
print('====================================================')

reminders5 = [x**2 % 5 for x in range(1, 51)]
print(reminders5)

print('====================================================')
print('====================================================')

reminders5 = [x**2 % 7 for x in range(1, 51)]
print(reminders5)

reminders5 = [x**2 % 12 for x in range(1, 51)]
print(reminders5)