# Flase
# None 
# Zero or any numric type
# Any empty sequence. Example : '', (), {}
# Any empty mapping: Example ()

test = False

if test:
	print('This is correct is True')
else:
	print('This is False')

test = None
print('\n None')
if test:
	print('This is  correct is True')
else:
	print('This is False')

test = ''
print("\n '' ")
if test:
	print('This is correct is True')
else:
	print('This is False')

test = ()
print('\n () ')
if test:
	print('This is correct is True')
else:
	print('This is False')

test = {}
print('\n {} ')
if test:
	print('This is correct is True')
else:
	print('This is False')

test = "Hello"
print('\n "" is not empty should be True')
if test:
	print('This is correct is True')
else:
	print('This is False')