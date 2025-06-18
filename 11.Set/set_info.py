test = set()
print(test)

print('')
print(dir(test))

'''
OUTPUT
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', 
'__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', 
'__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', 
'__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 
'__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''

print('to check line below')
# print(help(test.__rxor__))

print('')
test.add(17)
test.add(False)
test.add('Hello world')
test.add(32.76)
test.add(True)
print(test)

print('You can not add the same value or string tweice')
test.add('Hello world')
print(test)

print(len(test))

print('To remove any element use remove method')
test.remove(32.76)
print(test)

print(len(test))

# Another was to remove element in the test which is not exisit use discard
print('discard method will leave to continue without any error but remove will dispay an error\
		if the element is not in the test')
test.discard(12)
print(test)
