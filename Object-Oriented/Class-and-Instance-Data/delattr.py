# __delattr__ : Called when an attribute deletion is attempted.

class Product:
	attr = 2 
	
	# this function take only two parameters
	def __delattr__(self, name):
		print('Delete the instance {} from the methods '.format(str(name)))
		object.__delattr__(self, name)
		print('{} Deleted after called object'.format(str(name)))



inst = Product()

inst.name = 'Computer'
print('Give an instance name to the product: ', inst.name)

del inst.name 

#AttributeError: 'Product' object has no attribute 'name'
# print(inst.name)

print(inst.attr)

try:
	del inst.attr
except AttributeError as a:
	print('Deleted attr from methods {}'.format(a))

del Product.attr

try:
	print(Product.attr, '<')
except AttributeError:
	print('We can not display attr anymore because AttributeError Product has no more attribute attr!')
# print(Product.attr)