city = {'name':'Berlin','population':3.28, 'country': 'Germany', 'capital': True}
print(dir(city))

print(city.keys())
print(city.values())
# The methods are listed for dictionary are:
'''
clear()
copy()
fromkeys()
get()
items()
keys()
pop()
popitem()
setdefault()
update()
values()
'''
# how to use it:

new_city = city.copy()
the_city = dict.fromkeys(['name','population','county'])
print(the_city)
city.get('name')
city.items()
city.keys()
city.pop('capital')
print(city)
city.popitem()
city.setdefault('name','Berlin')
city.update({'name':'Berlin','population':3.28, 'county': 'Germany'})
city.values()

del city['population']
print(city)

city.clear()
print(city)