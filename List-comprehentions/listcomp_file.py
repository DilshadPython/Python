file = open('grades.txt')
grades = file.readlines()

print(grades)
# ['23\n', '45\n', '76\n', '34\n', '56\n', '98\n', '100\n', '30\n', '61\n', '77\n', '17']

print('****************************************************')
# to remove the \n 
for i in range(len(grades)):
	# rstrip() remove the \n
	grades[i] = grades[i].rstrip()
print(grades)

