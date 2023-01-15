
grades = [22, 44, 55, 33, 77, 12, 85, 17]

# only reading the list
for i in grades:
	print(i, ' ', end='')

# this is simmiler like list comperhensions but another way using for loops
for x in range(len(grades)):
	grades[x] = grades[x] + 8

print('\n', grades, end='')

print('\n#################################################')

print('This is a list comperhensions example all in one line')

listcomp = [x + 5 for x in grades]
print(listcomp)