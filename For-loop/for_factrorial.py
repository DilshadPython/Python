# 5! = 5*4*3*2*1
# 6! = 6 * 5!
# Factorial computation iteratively

num = int(input('Enter a number: '))
fact = 1

for i in range(1, num + 1):
	fact = fact * i
print(num,'! = ', fact)