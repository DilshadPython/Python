class People(dict):
	pass


obj = People()

obj['f'] = 'Female'
obj['m'] = 'Male'
obj['g'] = 'Girl'
obj['b'] = 'Boy'

for key in obj.keys():
	print('{} : {}'.format(key, obj[key]))
