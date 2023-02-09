first = ['a', 'b', 'c']
second = ['D', 'E', 'F']

thrid = first + second

print(thrid, ' << using + to add list')

print(first.__add__(second), ' << __add__(), to ad list')

tp1 = ('A', 'B', 'C')
tp2 = ('d', 'e', 'f')

tp3 = tp1 + tp2

print(tp3, ' << using + to add tuple')

print(tp1.__add__(tp2), ' << __add__() to add tuple')

dict1 = {'a': 11, 'b': 22, 'c': 33}
dict2 = {'D': 77, 'D': 66, 'E': 55}


try:
	print(dict1 + dict2 , ' << not working with dictionary')
except:
	print('We can not add tow dictionary toegther! using + or __add__ BUT another way')


result = {**dict1, **dict2}

print(result)