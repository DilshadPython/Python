# old style of 'Classic' class
class OldName():
	pass

# new style class
class NewClass(object):
	pass

# last style
class LastStyleClass:
	pass


oc = OldName()

nc = NewClass()

lsc = LastStyleClass()

print(type(oc)) # if use python2 display that <type <instance'>
print(type(nc))
print(type(lsc))
print('==========')

print(oc.__class__)
print(nc.__class__)
print(lsc.__class__)