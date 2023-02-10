class People(dict):

    def __setitem__(self, key, value):
        print('Setting a key and value')
        dict.__setitem__(self, key, value)


obj = People()

obj['f'] = 'Female'
obj['m'] = 'Male'
obj['g'] = 'Girl'
obj['b'] = 'Boy'

for key in obj.keys():
    print('{} : {}'.format(key, obj[key]))
