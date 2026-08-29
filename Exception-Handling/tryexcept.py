name = 'Dilshad Abdulla'

try:
	# we try to convert to int
	istring = int(name)
except:
	istring = -1

print('First ', istring)

name = '1973'
try:
	istring = int(name)
except:
	istring = -1

print('Second ', istring)