print('ints is narrower than longs')
print('longs is narrower than floats')
print('floats is narrower than complex')
print('')

print('Complex is wider than floats')
print('floats is wider than logns')
print('longs is wider than ints')

a = 8		#int
b = 17L		# longs
c = 7.13	# floats
d = 17 + 0j

# addtion
x = a + b # int + longs
print(x,  ' <<<<< rsults is longs float is wider than int')

# substraction
y = c - b # float - long
print(y, ' <<<<< rsults is float')

m = a * c # int * float
print(m, ' <<<<< the results is float')

# Division
z = d / c # complex / float 
print(z, '<<<< the rsults is complex')

