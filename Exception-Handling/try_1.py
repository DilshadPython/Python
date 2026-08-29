isnum = input('Enter a number: ')

try:
	testnum = int(isnum)
except:
	testnum = -1

if testnum > 0:
	print("Nice to check it's working :) ")
else:
	print("Sorry it's not working because it's not number !")