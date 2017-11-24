a = 'The new manager of Manchester united his name is '.split()
print(a)

print('\n#######################\n')
print(" The total length of all the words is '{}', you need to find out where do you want to insert\
	the name.".format(len(a)))

print('\n#######################\n')
a.insert(9, 'David Moyse.')
print(a)

print('\n#######################\n')
print( ' '.join(a))