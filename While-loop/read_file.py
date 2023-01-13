# we created a file named quote.txt 
# adding this numbers line by line 
# 12
# 27
# 98
# 13
# 45
# 16
# 97

count = 0
total = 0

thefile = open('qoutes.txt', 'r')
qoute = thefile.readline()

while (qoute):
	print(qoute)
	count = count + 1
	total = total + int(qoute)
	qoute = thefile.readline()

average = total / count
print('Average: ' + str(average))
