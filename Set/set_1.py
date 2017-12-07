#  What we try to achive here is to collecte the data but not the duplecate

alcohol_list = { 'Beer', 'Whiskey', 'Milk', 'Vodka', 'Beer', 'Whiskey', 'Rum', 'Cider', 'Milk' }

print('Display only one time the items: ')
print(alcohol_list)

print(type(alcohol_list))

print('--'*20)

if 'Beer' in alcohol_list:
	print('Yes Milk in the list')
else:
	print('No the drink is not in the list please buy it')